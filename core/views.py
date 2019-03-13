from builtins import super

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView, DetailView, FormView

from cart.models import Cart
from core.forms import AddReviewForm, SearchForm
from product.models import Brand, Category, Product, Comment


class BaseView(TemplateView):

    template_name = 'base.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        try:
            cart_id = self.request.session['cart_id']
            cart = Cart.objects.get(id=cart_id)
            self.request.session['total'] = cart.items.count()
        except:
            cart = Cart()
            cart.save()
            cart_id = cart.id
            self.request.session['cart_id'] = cart_id
            cart = Cart.objects.get(id=cart_id)

        context['cart'] = cart

        return context


class HomeView(ListView):

    template_name = 'homePage.html'
    model = Brand
    context_object_name = 'brands'
    ordering = ['order']
    paginate_by = 1

    queryset = Brand.objects.all().select_related('image_logo')

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        try:
            cart_id = self.request.session['cart_id']
            cart = Cart.objects.get(id=cart_id)
            self.request.session['total'] = cart.items.count()
        except:
            cart = Cart()
            cart.save()
            cart_id = cart.id
            self.request.session['cart_id'] = cart_id
            cart = Cart.objects.get(id=cart_id)

        context['cart'] = cart

        return context


class BrandsView(DetailView):

    template_name = 'brands.html'
    slug_field = 'name'
    model = Brand
    slug_url_kwarg = 'brand_name'

    def get_queryset(self):
        queryset = super(BrandsView, self).get_queryset()
        return queryset.select_related('image_women', 'image_men')

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(**kwargs)

        try:
            cart_id = self.request.session['cart_id']
            cart = Cart.objects.get(id=cart_id)
            self.request.session['total'] = cart.items.count()
        except:
            cart = Cart()
            cart.save()
            cart_id = cart.id
            self.request.session['cart_id'] = cart_id
            cart = Cart.objects.get(id=cart_id)

        context['cart'] = cart

        return context


class CategoriesView(TemplateView):

    template_name = 'categories.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        category = Category.objects.get_gender_category_by_name(name=self.kwargs['gender_category'])
        brand = Brand.objects.get_brand_by_name(name=self.kwargs['brand_name'])
        children_of_category = category.get_descendants()

        try:
            cart_id = self.request.session['cart_id']
            cart = Cart.objects.get(id=cart_id)
            self.request.session['total'] = cart.items.count()
        except:
            cart = Cart()
            cart.save()
            cart_id = cart.id
            self.request.session['cart_id'] = cart_id
            cart = Cart.objects.get(id=cart_id)

        context['cart'] = cart

        context.update({
            'category': category,
            'brand': brand,
            'children_of_category': children_of_category,
            'gender_category': category.get_root()
        })

        return context


def get_id_of_category_product_collection(category, brand):

    product_collection = []
    product_collection += Product.objects.get_product_by_category_and_brand(category=category, brand=brand)

    for child in category.get_descendants():
        product_collection += Product.objects.get_product_by_category_and_brand(category=child, brand=brand)

    id_collection = []

    for product in product_collection:
        id_collection.append(product.id)

    return id_collection


class ProductsView(TemplateView):

    template_name = 'products.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        cat = Category.objects.all().filter(name=self.kwargs['category'])
        brand = Brand.objects.get(name=self.kwargs['brand_name'])

        try:
            cart_id = self.request.session['cart_id']
            cart = Cart.objects.get(id=cart_id)
            self.request.session['total'] = cart.items.count()
        except:
            cart = Cart()
            cart.save()
            cart_id = cart.id
            self.request.session['cart_id'] = cart_id
            cart = Cart.objects.get(id=cart_id)

        for c in cat:
            if str(c.get_root()) == self.kwargs['gender_category']:
                cat = c

        product_collection = Product.objects.filter(id__in=get_id_of_category_product_collection(cat, brand))

        context.update({
            'product_collection': product_collection,
            'category': cat,
            'brand': brand,
            'gender_category': cat.get_root(),
            'cart': cart
        })

        if self.request.GET:
            context['form'] = SearchForm(data=self.request.GET)

            if context['form'].is_valid():
                context['product_collection'] = context['form'].get_search_queryset(context['product_collection'])
        else:
            context['form'] = SearchForm()
            # initial = {'lowest_price': 0.00}

        return context


class DetailProductView(DetailView):

    template_name = 'detail_product.html'

    def get_object(self, queryset=None):

        name = self.kwargs.get('product_name')

        return get_object_or_404(Product, name=name)

    def get_context_data(self, **kwargs):

        try:
            cart_id = self.request.session['cart_id']
            cart = Cart.objects.get(id=cart_id)
            self.request.session['total'] = cart.items.count()
        except:
            cart = Cart()
            cart.save()
            cart_id = cart.id
            self.request.session['cart_id'] = cart_id
            cart = Cart.objects.get(id=cart_id)

        context = super().get_context_data(**kwargs)
        context['reviews'] = Comment.comment_manager.get_comment_by_product(product=self.object)
        context['cart'] = cart

        return context


@method_decorator(login_required, 'dispatch')
class AddReviewView(FormView):

    template_name = 'add_review.html'
    form_class = AddReviewForm

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        try:
            cart_id = self.request.session['cart_id']
            cart = Cart.objects.get(id=cart_id)
            self.request.session['total'] = cart.items.count()
        except:
            cart = Cart()
            cart.save()
            cart_id = cart.id
            self.request.session['cart_id'] = cart_id
            cart = Cart.objects.get(id=cart_id)

        context['cart'] = cart

        return context

    def form_valid(self, form):
        product = Product.objects.get(id=self.request.GET['product_id'])
        parent_obj = None
        try:
            parent_id = int(self.request.GET['parent_id'])
        except:
            parent_id = None
        if parent_id:
            parent_obj = Comment.comment_manager.get(id=parent_id)
            if parent_obj:
                replay_comment = form.save(user=self.request.user, product=product, parent=parent_obj)
                replay_comment.parent = parent_obj
        else:
            form.save(user=self.request.user, product=product, parent=parent_obj)

        return redirect('core:product',
                        brand_name=product.brand.name,
                        gender_category=product.category.get_root(),
                        category=product.category,
                        product_name=product.name)


@method_decorator(login_required, 'dispatch')
class EditReviewView(AddReviewView):

    def get_form_kwargs(self):

        kwargs = super().get_form_kwargs()
        kwargs['instance'] = get_object_or_404(Comment, id=self.kwargs['review_id'], author=self.request.user)

        return kwargs
