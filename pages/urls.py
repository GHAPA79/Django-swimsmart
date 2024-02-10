from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('usa-method/', views.USAMethod.as_view(), name='usa-method'),
    path('aus-method/', views.AUSMethod.as_view(), name='aus-method'),
    path('uk-method/', views.UKMethod.as_view(), name='uk-method'),
    path('chn-method/', views.CHNMethod.as_view(), name='chn-method'),
    path('about-methods/', views.AboutMethods.as_view(), name='about-methods'),
    path('guide-exercise/', views.GuideExercise.as_view(), name='guide-exercise'),
    path('warm-up-and-cold-down/', views.WarmUpAndColdDown.as_view(), name='warm-up-and-cold-down'),
]
