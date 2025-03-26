from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'home.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class GymView(TemplateView):
    template_name = 'gym.html'


class USAMethod(TemplateView):
    template_name = 'usa.html'


class AUSMethod(TemplateView):
    template_name = 'aus.html'


class UKMethod(TemplateView):
    template_name = 'uk.html'


class CHNMethod(TemplateView):
    template_name = 'chn.html'


class AboutMethods(TemplateView):
    template_name = 'about-methods.html'


class GuideExercise(TemplateView):
    template_name = 'guide-exercise.html'


class WarmUpAndColdDown(TemplateView):
    template_name = 'warm-up-and-cold-down.html'
