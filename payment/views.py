import requests
import json

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from django.http import HttpResponse

from orders.models import Order


def payment_process_view(request):
    # Get order_id from session
    order_id = request.session.get('order_id')
    # Get the order object
    order = get_object_or_404(Order, id=order_id)
    # Get total price from order
    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    # Request to ZarinPal
    zarinpal_request_url = 'https://api.zarinpal.com/pg/v4/payment/request.json'

    request_data = {
        'merchant_id': settings.ZARINPAL_MERCHANT_ID,
        'amount': rial_total_price,
        'description': f'#{order.id}: {order.first_name} {order.last_name}',
        'callback_url': request.build_absolute_uri(reverse('payment:payment_callback')),
    }

    request_header = {
        'accept': 'application/json',
        'content-type': 'application/json',
    }

    response = requests.post(url=zarinpal_request_url, data=json.dumps(request_data), headers=request_header)

    data = response.json()['data']
    authority = data['authority']
    order.zarinpal_authority = authority
    order.save()

    if 'errors' not in data or len(data['errors']) == 0:
        return redirect(f'https://www.zarinpal.com/pg/StartPay/{authority}')
    else:
        return HttpResponse('Error from ZarinPal')


def payment_callback_view(request):
    # Get authority from request
    payment_authority = request.GET.get('authority')
    # Get status from request
    payment_status = request.GET.get('status')
    # Get order with zarinpal_authority
    order = get_object_or_404(Order, zarinpal_authority=payment_authority)
    # Get price from order
    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    # Verifying payment status
    if payment_status == 'OK':
        request_data = {
            'merchant_id': settings.ZARINPAL_MERCHANT_ID,
            'amount': rial_total_price,
            'authority': payment_authority,
        }

        request_header = {
            'accept': 'application/json',
            'content-type': 'application/json',
        }

        response = requests.post(
            url='https://api.zarinpal.com/pg/v4/payment/verify.json',
            data=json.dumps(request_data),
            headers=request_header,
        )

        # Verifying payment code
        if 'data' in response.json() and ('errors' not in response.json()['data'] or len(response.json()['data']['errors']) == 0):
            data = response.json()['data']
            payment_code = data['code']

            if payment_code == 100:
                order.is_paid = True
                order.ref_id = data['ref_id']
                order.zarinpal_user_data = data
                order.save()

                return HttpResponse('پرداخت با موفقیت انجام شد')

            elif payment_code == 101:
                return HttpResponse('پرداخت با موفقیت انجام شد. البته این تراکنش قبلا ثبت شده است')

            else:
                error_code = response.json()['errors']['code']
                error_message = response.json()['errors']['message']
                return HttpResponse(f' تراکنش ناموفق بود {error_code} {error_message}')

    else:
        return HttpResponse('تراکنش ناموفق بود')
