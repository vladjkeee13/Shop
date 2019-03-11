from django.urls import path

from cart.views import CartView, AddToCartView, RemoveItemFromCartView

urlpatterns = [
    path('cart', CartView.as_view(), name='cart'),
    path('add-to-cart', AddToCartView.as_view(), name='add-to-cart'),
    path('remove-item-from-cart', RemoveItemFromCartView.as_view(), name='remove-item-from-cart')
]
