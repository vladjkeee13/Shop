from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from product.models import Brand


class HomeView(TemplateView):
    template_name = 'homePage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brands = Brand.objects.all()
        context.update(
            {
                'brands': brands
            }
        )
        return context


class JackWolfsinViews(TemplateView):
    template_name = 'Brands/JackWolfskin.html'


class TheNorthFaceView(TemplateView):
    template_name = 'Brands/TheNorthFace.html'


class BerghausView(View):

    def get(self, request):
        return render(request, 'Brands/Berghaus.html')
