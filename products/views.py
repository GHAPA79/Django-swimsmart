from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .forms import ContactForm
from .models import Product, Contact


class ContactCreateView(SuccessMessageMixin, generic.CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact')
    success_message = 'پیام شما با موفقیت ثبت گردید. پس از تایید از طرف ادمین پاسخ و نمایش داده خواهد شد'


class USAMethodFast(generic.ListView):
    queryset = Product.objects.filter(category_id=1)
    template_name = 'usa-fast.html'
    context_object_name = 'products'
