from django.urls import path

from . import views

urlpatterns = [
    path('usa-method-fast/', views.USAMethodFast.as_view(), name='usa-method-fast'),
    path('usa-method-semi-endu/', views.USAMethodSemiEndu.as_view(), name='usa-method-semi-endu'),
    path('usa-method-endu/', views.USAMethodEndu.as_view(), name='usa-method-endu'),
]
