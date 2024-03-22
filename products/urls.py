from django.urls import path

from . import views

urlpatterns = [
    path('usa-method-fast/', views.USAMethodFast.as_view(), name='usa-method-fast'),
    path('usa-method-semi-endu/', views.USAMethodSemiEndu.as_view(), name='usa-method-semi-endu'),
    path('usa-method-endu/', views.USAMethodEndu.as_view(), name='usa-method-endu'),
    path('aus-method-fast/', views.AUSMethodFast.as_view(), name='aus-method-fast'),
    path('aus-method-semi-endu/', views.AUSMethodSemiEndu.as_view(), name='aus-method-semi-endu'),
    path('aus-method-endu/', views.AUSMethodEndu.as_view(), name='aus-method-endu'),
    path('uk-method-fast/', views.UKMethodFast.as_view(), name='uk-method-fast'),
    path('uk-method-semi-endu/', views.UKMethodSemiEndu.as_view(), name='uk-method-semi-endu'),
    path('uk-method-endu/', views.UKMethodEndu.as_view(), name='uk-method-endu'),
    path('chn-method-fast/', views.CHNMethodFast.as_view(), name='chn-method-fast'),
    path('chn-method-semi-endu/', views.CHNMethodSemiEndu.as_view(), name='chn-method-semi-endu'),
    path('chn-method-endu/', views.CHNMethodEndu.as_view(), name='chn-method-endu'),
    path('pdf-purchased/', views.pdf_purchased_view, name='pdf-purchased'),
]
