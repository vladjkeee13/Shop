from django.urls import path
from core.views import HomeView, JackWolfsinViews, TheNorthFaceView, BerghausView

urlpatterns = [
    path('', HomeView.as_view()),
    path('jack-wolfskin/', JackWolfsinViews.as_view(), name='jack-wolfskin'),
    path('the-north-face/', TheNorthFaceView.as_view(), name='the-north-face'),
    path('berghaus/', BerghausView.as_view(), name='berghaus')
]
