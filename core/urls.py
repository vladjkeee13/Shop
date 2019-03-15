from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from core.views import HomeView, BrandsView, CategoriesView, ProductsView, DetailProductView, AddReviewView, \
    EditReviewView, RegistrationView, LoginView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('brand/<str:brand_name>', BrandsView.as_view(), name='brand'),
    path('brand/<str:brand_name>/<str:gender_category>', CategoriesView.as_view(), name='categories'),
    path('brand/<str:brand_name>/<str:gender_category>/<str:category>', ProductsView.as_view(), name='products'),
    path('brand/<str:brand_name>/<str:gender_category>/<str:category>/<str:product_name>',
         DetailProductView.as_view(), name='product'),
    path('add-review', AddReviewView.as_view(), name='add_review'),
    path('edit-review/<int:review_id>', EditReviewView.as_view(), name='edit-review'),
    path('registration', RegistrationView.as_view(), name='registration'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page=reverse_lazy('core:index')), name='logout')
]
