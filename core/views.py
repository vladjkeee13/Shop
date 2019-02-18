from django.views.generic import TemplateView, ListView

from product.models import Brand


class HomeView(ListView):
    template_name = 'homePage.html'
    model = Brand
    context_object_name = 'brands'


class JackWolfsinViews(ListView):
    template_name = 'Brands/JackWolfskin.html'
    model = Brand
    context_object_name = 'brands'

    def get_queryset(self):
        return self.model.objects.filter(name='Jack Wolfskin')


class TheNorthFaceView(ListView):
    template_name = 'Brands/TheNorthFace.html'
    model = Brand
    context_object_name = 'brands'

    def get_queryset(self):
        return self.model.objects.filter(name='The North Face')


class BerghausView(ListView):
    template_name = 'Brands/Berghaus.html'
    model = Brand
    context_object_name = 'brands'

    def get_queryset(self):
        return self.model.objects.filter(name='Berghaus')
