from django.urls import path

from . import views

urlpatterns = [
    path('usa-method-fast/', views.USAMethodFast.as_view(), name='usa-method-fast'),
    path('usa-method-semi-endu/', views.USAMethodSemiEndu.as_view(), name='usa-method-semi-endu'),
    path('usa-method-endu/', views.USAMethodEndu.as_view(), name='usa-method-endu'),
    path('aus-method-fast/', views.AUSMethodFast.as_view(), name='aus-method-fast'),
    path('aus-method-semi-endu/', views.AUSMethodSemiEndu.as_view(), name='aus-method-semi-endu'),
    path('aus-method-endu/', views.AUSMethodEndu.as_view(), name='aus-method-endu'),

]
