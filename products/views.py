from django.views import generic

from .models import Product


class USAMethodFast(generic.ListView):
    queryset = Product.objects.filter(category_id=1)
    template_name = 'usa-fast.html'
    context_object_name = 'products'
