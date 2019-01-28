from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'homePage.html'


class JackWolfsinViews(TemplateView):
    template_name = 'Brands/JackWolfskin.html'


class TheNorthFaceView(TemplateView):
    template_name = 'Brands/TheNorthFace.html'

#
# class BerghausView(TemplateView):
#     template_name = 'Brands/Berghaus.html'


class BerghausView(View):

    def get(self, request):
        return render(request, 'Brands/Berghaus.html')
