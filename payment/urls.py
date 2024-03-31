from django.urls import path

from . import views

app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process_view, name='payment_process'),
    path('callback/', views.payment_callback_view, name='payment_callback'),
    path('unsuccessful-payment/', views.unsuccessful_payment_view, name='unsuccessful_payment'),
    path('unsuccessful-payment-from-gateway/', views.unsuccessful_payment_from_gateway_view, name='unsuccessful_payment_from_gateway'),
]
