from django.shortcuts import render

from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'home.html'


class USAMethod(TemplateView):
    template_name = 'usa.html'


class AUSMethod(TemplateView):
    template_name = 'aus.html'


class UKMethod(TemplateView):
    template_name = 'uk.html'


class CHNMethod(TemplateView):
    template_name = 'chn.html'
