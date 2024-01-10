from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('usa-method/', views.USAMethod.as_view(), name='usa-method'),
    path('aus-method/', views.AUSMethod.as_view(), name='aus-method'),
    path('uk-method/', views.UKMethod.as_view(), name='uk-method'),
    path('chn-method/', views.CHNMethod.as_view(), name='chn-method'),
]
