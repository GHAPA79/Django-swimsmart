from django.urls import path

from . import views

urlpatterns = [
    path('usa-method-fast/', views.USAMethodFast.as_view(), name='usa-method-fast'),
]
