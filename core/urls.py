from django.urls import path
from core.views import HomeView, BrandsView

urlpatterns = [
    path('', HomeView.as_view()),
    path('brand/<int:pk>', BrandsView.as_view(), name='brand'),

]
