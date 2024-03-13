import requests
import json

from django.shortcuts import get_object_or_404, redirect, reverse
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
    zibal_request_url = 'https://gateway.zibal.ir/v1/request'

    request_data = {
        "merchant": "zibal",
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
    order.zarinpal_authority = trackId
    order.save()

    if result == 100:
        return redirect(f'https://gateway.zibal.ir/start/{trackId}')
    else:
        return HttpResponse('Error from zibal')


def payment_callback_view(request):
    # Get authority from request
    payment_trackId = request.GET.get('trackId')
    # Get status from request
    payment_status = request.GET.get('status')
    # Get order with zarinpal_authority
    order = get_object_or_404(Order, zarinpal_authority=payment_trackId)
    # Get price from order
    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    # Verifying payment status
    if payment_status == 1:
        request_data = {
            "merchant": "zibal",
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
        payment_code = data["result"]

        if payment_code == 100:
            order.is_paid = True
            order.ref_id = data["refNumber"]
            order.zarinpal_user_data = data
            order.save()

            return HttpResponse('پرداخت با موفقیت انجام شد')

        elif payment_code == 201:
            return HttpResponse('پرداخت با موفقیت انجام شد. البته این تراکنش قبلا ثبت شده است')

        else:
            error_message = response.json()["message"]
            return HttpResponse(f' تراکنش ناموفق بود {error_message}')

    else:
        return HttpResponse('تراکنش ناموفق بود')
