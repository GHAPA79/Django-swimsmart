from django.views import generic

from .models import Product


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
