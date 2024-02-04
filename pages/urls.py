from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('usa-method/', views.USAMethod.as_view(), name='usa-method'),
    path('aus-method/', views.AUSMethod.as_view(), name='aus-method'),
    path('uk-method/', views.UKMethod.as_view(), name='uk-method'),
    path('chn-method/', views.CHNMethod.as_view(), name='chn-method'),
    path('uk-method-fast/', views.UKMethodFast.as_view(), name='uk-method-fast'),
    path('uk-method-semi-endu/', views.UKMethodSemiEndu.as_view(), name='uk-method-semi-endu'),
    path('uk-method-endu/', views.UKMethodEndu.as_view(), name='uk-method-endu'),
    path('chn-method-fast/', views.CHNMethodFast.as_view(), name='chn-method-fast'),
    path('chn-method-semi-endu/', views.CHNMethodSemiEndu.as_view(), name='chn-method-semi-endu'),
    path('chn-method-endu/', views.CHNMethodEndu.as_view(), name='chn-method-endu'),
]
