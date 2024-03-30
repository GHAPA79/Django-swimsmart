from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages

from products.models import Product
from .cart import Cart
from .forms import AddToCartProductForm


def cart_detail_view(request):
    cart = Cart(request)

    return render(request, 'cart_detail.html', context={'cart': cart})


@require_POST
def add_to_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    cart_form = AddToCartProductForm(request.POST)

    if cart_form.is_valid():
        cleaned_data = cart_form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity)

    return redirect('cart:cart-detail')


def remove_from_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)

    cart.remove(product)

    return redirect('cart:cart-detail')


@require_POST
def clear_cart(request):
    cart = Cart(request)

    if len(cart):
        cart.clear()
        messages.success(request, 'همه ی تمرینات از سبد خرید حذف شدند')
    else:
        messages.success(request, '! سبد خرید شما خالی است')

    return redirect('cart:cart-detail')
