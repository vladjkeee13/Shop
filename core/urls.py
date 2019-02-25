from django.urls import path
from core.views import HomeView, BrandsView, CategoriesView, ProductsView, DetailProductView

urlpatterns = [
    path('', HomeView.as_view()),
    path('brand/<str:brand_name>', BrandsView.as_view(), name='brand'),
    path('brand/<str:brand_name>/<str:gender_category>', CategoriesView.as_view(), name='categories'),
    path('brand/<str:brand_name>/<str:gender_category>/<str:category>', ProductsView.as_view(), name='products'),
    path('brand/<str:brand_name>/<str:gender_category>/<str:category>/<str:product_name>',
         DetailProductView.as_view(), name='product')
]
