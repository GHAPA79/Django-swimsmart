import requests
import json

from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.conf import settings
from django.contrib import messages

from orders.models import Order


def payment_process_view(request):
    # Get order_id from session
    order_id = request.session.get('order_id')
    # Get the order object
    order = get_object_or_404(Order, id=order_id)
    # Get total price from order
    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    # Request to Zibal
    zibal_request_url = 'https://gateway.zibal.ir/v1/request'

    request_data = {
        "merchant": settings.ZIBAL_MERCHANT_ID,
        "amount": rial_total_price,
        "callbackUrl": request.build_absolute_uri(reverse('payment:payment_callback')),
        "description": f'#{order.id}: {order.first_name} {order.last_name}',
        "mobile": order.phone_number,
    }

    request_header = {
        'accept': 'application/json',
        'content-type': 'application/json',
    }

    response = requests.post(url=zibal_request_url, data=json.dumps(request_data), headers=request_header)

    data = response.json()
    trackId = data["trackId"]
    result = data["result"]
    order.zibal_authority = trackId
    order.save()

    if result == 100:
        return redirect(f'https://gateway.zibal.ir/start/{trackId}')
    else:
        return redirect('payment:unsuccessful_payment_from_gateway')


def payment_callback_view(request):
    # Get authority from request
    payment_trackId = request.GET.get('trackId')
    # Get status from request
    payment_status = request.GET.get('status')
    # Get order with zarinpal_authority
    order = get_object_or_404(Order, zibal_authority=payment_trackId)
    # Get price from order
    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    # Verifying payment status
    request_data = {
        "merchant": settings.ZIBAL_MERCHANT_ID,
        "trackId": payment_trackId,
    }

    request_header = {
        'accept': 'application/json',
        'content-type': 'application/json',
    }

    response = requests.post(
        url='https://gateway.zibal.ir/v1/verify',
        data=json.dumps(request_data),
        headers=request_header,
    )

    # Verifying payment code
    data = response.json()
    payment_message = data["message"]

    if payment_message == "success":
        order.is_paid = True
        order.zibal_ref_id = data["refNumber"]
        order.zibal_user_data = data
        order.save()

        messages.success(request, 'پرداخت با موفقیت انجام شد')
        messages.info(request, 'لینک دوره در صفحه "پروفایل / لینک دوره های خریداری شده" قابل دسترسی می باشد')
        return redirect('pdf-purchased')

    else:
        return redirect('payment:unsuccessful_payment')


def unsuccessful_payment_view(request):
    return render(request, 'unsuccessful_payment.html')


def unsuccessful_payment_from_gateway_view(request):
    return render(request, 'unsuccessful_payment_from_gateway.html')
