from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.Profile.as_view(), name='profile'),
]
