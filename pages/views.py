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


class USAMethodFast(TemplateView):
    template_name = 'usa-fast.html'


class USAMethodSemiEndu(TemplateView):
    template_name = 'usa-semi-en.html'


class USAMethodEndu(TemplateView):
    template_name = 'usa-endu.html'


class AUSMethodFast(TemplateView):
    template_name = 'aus-fast.html'


class AUSMethodSemiEndu(TemplateView):
    template_name = 'aus-semi-en.html'


class AUSMethodEndu(TemplateView):
    template_name = 'aus-endu.html'


class UKMethodFast(TemplateView):
    template_name = 'uk-fast.html'


class UKMethodSemiEndu(TemplateView):
    template_name = 'uk-semi-en.html'


class UKMethodEndu(TemplateView):
    template_name = 'uk-endu.html'


class CHNMethodFast(TemplateView):
    template_name = 'chn-fast.html'


class CHNMethodSemiEndu(TemplateView):
    template_name = 'chn-semi-en.html'


class CHNMethodEndu(TemplateView):
    template_name = 'chn-endu.html'
