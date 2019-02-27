from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView

from product.models import Brand, Category, Product


class HomeView(ListView):

    template_name = 'homePage.html'
    model = Brand
    context_object_name = 'brands'
    ordering = ['order']

    queryset = Brand.objects.all().select_related('image_logo')


class BrandsView(DetailView):

    template_name = 'brands.html'

    def get_object(self, queryset=None):
        name = self.kwargs.get("brand_name")

        return get_object_or_404(Brand, name=name)


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


class DetailProductView(TemplateView):

    template_name = 'detail_product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(name=self.kwargs['product_name'])

        context.update({
            'product': product
        })

        return context
