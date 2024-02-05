from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'home.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class USAMethod(TemplateView):
    template_name = 'usa.html'


class AUSMethod(TemplateView):
    template_name = 'aus.html'


class UKMethod(TemplateView):
    template_name = 'uk.html'


class CHNMethod(TemplateView):
    template_name = 'chn.html'


class CHNMethodFast(TemplateView):
    template_name = 'chn-fast.html'


class CHNMethodSemiEndu(TemplateView):
    template_name = 'chn-semi-en.html'


class CHNMethodEndu(TemplateView):
    template_name = 'chn-endu.html'

