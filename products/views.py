from django.views import generic
from django.shortcuts import render
from django.http import HttpResponseForbidden

from .models import Product, PurchaseFile
from orders.models import OrderItem
from cart.forms import AddToCartProductForm


class USAMethodFast(generic.ListView):
    queryset = Product.objects.filter(category_id=1)
    template_name = 'usa-fast.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_to_cart_form'] = AddToCartProductForm
        return context


class USAMethodSemiEndu(generic.ListView):
    queryset = Product.objects.filter(category_id=2)
    template_name = 'usa-semi-en.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_to_cart_form'] = AddToCartProductForm
        return context


class USAMethodEndu(generic.ListView):
    queryset = Product.objects.filter(category_id=3)
    template_name = 'usa-endu.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_to_cart_form'] = AddToCartProductForm
        return context


class UKMethodFast(generic.ListView):
    queryset = Product.objects.filter(category_id=4)
    template_name = 'uk-fast.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_to_cart_form'] = AddToCartProductForm
        return context


class UKMethodSemiEndu(generic.ListView):
    queryset = Product.objects.filter(category_id=5)
    template_name = 'uk-semi-en.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_to_cart_form'] = AddToCartProductForm
        return context


class UKMethodEndu(generic.ListView):
    queryset = Product.objects.filter(category_id=6)
    template_name = 'uk-endu.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_to_cart_form'] = AddToCartProductForm
        return context


class AUSMethodFast(generic.ListView):
    queryset = Product.objects.filter(category_id=7)
    template_name = 'aus-fast.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_to_cart_form'] = AddToCartProductForm
        return context


class AUSMethodSemiEndu(generic.ListView):
    queryset = Product.objects.filter(category_id=8)
    template_name = 'aus-semi-en.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_to_cart_form'] = AddToCartProductForm
        return context


class AUSMethodEndu(generic.ListView):
    queryset = Product.objects.filter(category_id=9)
    template_name = 'aus-endu.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_to_cart_form'] = AddToCartProductForm
        return context


class CHNMethodFast(generic.ListView):
    queryset = Product.objects.filter(category_id=10)
    template_name = 'chn-fast.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_to_cart_form'] = AddToCartProductForm
        return context


class CHNMethodSemiEndu(generic.ListView):
    queryset = Product.objects.filter(category_id=11)
    template_name = 'chn-semi-en.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_to_cart_form'] = AddToCartProductForm
        return context


class CHNMethodEndu(generic.ListView):
    queryset = Product.objects.filter(category_id=12)
    template_name = 'chn-endu.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_to_cart_form'] = AddToCartProductForm
        return context
    

class GymWoman(generic.ListView):
    queryset = Product.objects.filter(category_id=13)
    template_name = 'gym-woman.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_to_cart_form'] = AddToCartProductForm
        return context
    

class GymMen(generic.ListView):
    queryset = Product.objects.filter(category_id=14)
    template_name = 'gym-man.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_to_cart_form'] = AddToCartProductForm
        return context


def pdf_purchased_view(request):
    order_items = OrderItem.objects.filter(order__user=request.user, order__is_paid=True)
    product_ids = []
    for order_item in order_items:
        product_ids.append(order_item.product.id)

    pdf_purchased = PurchaseFile.objects.filter(product_id__in=product_ids)

    if not pdf_purchased:
        HttpResponseForbidden("شما اجازه دسترسی به این صفحه را ندارید")

    return render(request, 'purchased_user_links.html', context={'pdfs': pdf_purchased})
