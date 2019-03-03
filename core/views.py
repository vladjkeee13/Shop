from builtins import super

from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, DetailView

from core.forms import AddReviewForm
from product.models import Brand, Category, Product, Comment


class HomeView(ListView):

    template_name = 'homePage.html'
    model = Brand
    context_object_name = 'brands'
    ordering = ['order']

    queryset = Brand.objects.all().select_related('image_logo')


class BrandsView(DetailView):

    template_name = 'brands.html'
    slug_field = 'name'
    model = Brand
    slug_url_kwarg = 'brand_name'

    def get_queryset(self):
        queryset = super(BrandsView, self).get_queryset()
        return queryset.select_related('image_women', 'image_men')


class CategoriesView(TemplateView):

    template_name = 'categories.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        category = Category.objects.get(name=self.kwargs['gender_category'])
        brand = Brand.objects.get(name=self.kwargs['brand_name'])
        children_of_category = category.get_descendants()

        context.update({
            'category': category,
            'brand': brand,
            'children_of_category': children_of_category,
            'gender_category': category.get_root()
        })

        return context


def get_category_product_collection(category, brand):

    product_collection = []
    product_collection += Product.objects.filter(category=category, brand=brand)

    for child in category.get_descendants():
        product_collection += Product.objects.filter(category=child, brand=brand)

    return product_collection


class ProductsView(TemplateView):

    template_name = 'products.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        cat = Category.objects.all().filter(name=self.kwargs['category'])
        brand = Brand.objects.get(name=self.kwargs['brand_name'])

        for c in cat:
            if str(c.get_root()) == self.kwargs['gender_category']:
                cat = c

        context.update({
            'product_collection': get_category_product_collection(cat, brand),
            'category': cat,
            'brand': brand,
            'gender_category': cat.get_root()
        })

        return context


class DetailProductView(DetailView):

    template_name = 'detail_product.html'

    def get_object(self, queryset=None):

        name = self.kwargs.get('product_name')

        return get_object_or_404(Product, name=name)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['reviews'] = Comment.objects.filter(parent__isnull=True,
                                                    product=Product.objects.get(name=self.kwargs.get('product_name')))

        return context


class AddReviewView(TemplateView):

    template_name = 'add_review.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['form'] = AddReviewForm()

        return context

    def post(self, request):

        context = self.get_context_data()
        form = AddReviewForm(request.POST)
        product = Product.objects.get(id=request.GET['product_id'])
        context['form'] = form

        if form.is_valid():
            parent_obj = None
            try:
                parent_id = int(request.GET['parent_id'])
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                if parent_obj:
                    replay_comment = form.save(request.user, product, parent_obj)
                    replay_comment.parent = parent_obj
            else:
                form.save(request.user, product, parent_obj)

            return redirect('core:product',
                            brand_name=product.brand.name,
                            gender_category=product.category.get_root(),
                            category=product.category,
                            product_name=product.name)

        return self.render_to_response(context)
