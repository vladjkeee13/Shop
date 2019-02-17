from django.views.generic import TemplateView, ListView

from product.models import Brand


class HomeView(ListView):
    template_name = 'homePage.html'
    model = Brand
    context_object_name = 'brands'


class JackWolfsinViews(TemplateView):
    template_name = 'Brands/JackWolfskin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brands = Brand.objects.filter(name='Jack Wolfskin')
        context.update({
            'brands': brands
        })
        return context


class TheNorthFaceView(TemplateView):
    template_name = 'Brands/TheNorthFace.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brands = Brand.objects.filter(name='The North Face')
        context.update({
            'brands': brands
        })
        return context


class BerghausView(TemplateView):
    template_name = 'Brands/Berghaus.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brands = Brand.objects.filter(name='Berghaus')
        context.update({
            'brands': brands
        })
        return context
