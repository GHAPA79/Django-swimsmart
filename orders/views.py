from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import OrderForm
from cart.cart import Cart
from .models import OrderItem


@login_required
def order_create_view(request):
    order_form = OrderForm()
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, 'سبد خرید شما خالی است | حداقل یک تمرین باید در سبد خرید شما باشد')
        return redirect('home')

    if request.method == 'POST':
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.select_related('order__user').create(
                    order=order_obj,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price,
                )

            cart.clear()

            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.email = order_obj.email
            request.user.save()

            request.session['order_id'] = order_obj.id
            return HttpResponseRedirect(reverse('payment:payment_process'))

    return render(request, 'order_create.html', context={'form': order_form})
