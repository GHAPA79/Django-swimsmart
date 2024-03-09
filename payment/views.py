import requests
import json

from django.shortcuts import render, get_object_or_404
from django.conf import settings

from orders.models import Order


def payment_process(request):
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
        'callback_url': '127.0.0.1:8000',
    }

    request_header = {
        'accept': 'application/json',
        'content-type': 'application/json',
    }

    response = requests.post(url=zarinpal_request_url, data=json.dumps(request_data), headers=request_header)
