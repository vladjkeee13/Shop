from django.shortcuts import redirect
from django.views import View
from django.views.generic import DetailView

from cart.models import Cart
from product.models import Product


class CartView(DetailView):

    template_name = 'cart.html'

    def get_object(self, queryset=None):

        try:
            cart_id = self.request.session['cart_id']
            cart = Cart.objects.get(id=cart_id)
            self.request.session['total'] = cart.items.count()
        except:
            cart = Cart()
            cart.save()
            cart_id = cart.id
            self.request.session['cart_id'] = cart_id
            cart = Cart.objects.get(id=cart_id)

        return cart


class AddToCartView(View):

    def get(self, request):

        try:
            cart_id = self.request.session['cart_id']
            cart = Cart.objects.get(id=cart_id)
            self.request.session['total'] = cart.items.count()
        except:
            cart = Cart()
            cart.save()
            cart_id = cart.id
            self.request.session['cart_id'] = cart_id
            cart = Cart.objects.get(id=cart_id)

        product = Product.objects.get(id=request.GET['product_id'])
        cart.add_to_cart(product)

        return redirect('cart:cart')


class RemoveItemFromCartView(View):

    def get(self, request):

        try:
            cart_id = self.request.session['cart_id']
            cart = Cart.objects.get(id=cart_id)
            self.request.session['total'] = cart.items.count()
        except:
            cart = Cart()
            cart.save()
            cart_id = cart.id
            self.request.session['cart_id'] = cart_id
            cart = Cart.objects.get(id=cart_id)

        product = Product.objects.get(id=request.GET['product_id'])
        cart.remove_from_cart(product)

        return redirect('cart:cart')
