from django.views.generic import ListView, DetailView

from product.models import Brand


class HomeView(ListView):
    template_name = 'homePage.html'
    model = Brand
    context_object_name = 'brands'


class BrandsView(DetailView):
    template_name = 'brands.html'
    queryset = Brand.objects.all()
