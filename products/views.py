from django.views import generic
from django.shortcuts import render

from .models import Product
from accounts.models import CustomUser


class USAMethodFast(generic.ListView):
    queryset = Product.objects.filter(category_id=1)
    template_name = 'usa-fast.html'
    context_object_name = 'products'


class USAMethodSemiEndu(generic.ListView):
    queryset = Product.objects.filter(category_id=5)
    template_name = 'usa-semi-en.html'
    context_object_name = 'products'


class USAMethodEndu(generic.ListView):
    queryset = Product.objects.filter(category_id=9)
    template_name = 'usa-endu.html'
    context_object_name = 'products'


class AUSMethodFast(generic.ListView):
    queryset = Product.objects.filter(category_id=3)
    template_name = 'aus-fast.html'
    context_object_name = 'products'


class AUSMethodSemiEndu(generic.ListView):
    queryset = Product.objects.filter(category_id=7)
    template_name = 'aus-semi-en.html'
    context_object_name = 'products'


class AUSMethodEndu(generic.ListView):
    queryset = Product.objects.filter(category_id=11)
    template_name = 'aus-endu.html'
    context_object_name = 'products'


class UKMethodFast(generic.ListView):
    queryset = Product.objects.filter(category_id=2)
    template_name = 'uk-fast.html'
    context_object_name = 'products'


class UKMethodSemiEndu(generic.ListView):
    queryset = Product.objects.filter(category_id=6)
    template_name = 'uk-semi-en.html'
    context_object_name = 'products'


class UKMethodEndu(generic.ListView):
    queryset = Product.objects.filter(category_id=10)
    template_name = 'uk-endu.html'
    context_object_name = 'products'


class CHNMethodFast(generic.ListView):
    queryset = Product.objects.filter(category_id=4)
    template_name = 'chn-fast.html'
    context_object_name = 'products'


class CHNMethodSemiEndu(generic.ListView):
    queryset = Product.objects.filter(category_id=8)
    template_name = 'chn-semi-en.html'
    context_object_name = 'products'


class CHNMethodEndu(generic.ListView):
    queryset = Product.objects.filter(category_id=12)
    template_name = 'chn-endu.html'
    context_object_name = 'products'


class DownloadExercise(generic.ListView):
    queryset = Product.objects.all()
    template_name = 'purchased_user_links.html'
    context_object_name = 'products'

    def get_object(self, queryset=None):
        return CustomUser.objects.get(pk=self.request.user.pk)
