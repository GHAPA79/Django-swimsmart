from django.urls import path

from . import views

urlpatterns = [
    path('contact/', views.ContactCreateView.as_view(), name='contact'),
    path('usa-method-fast/', views.USAMethodFast.as_view(), name='usa-method-fast'),
]
