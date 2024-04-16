from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .forms import CustomUserCreationForm, ProfileForm
from .models import CustomUser


class SignUpView(SuccessMessageMixin, generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    success_message = 'حساب کاربری شما با موفقیت ساخته شد. لطفا وارد شوید'


class Profile(SuccessMessageMixin, generic.UpdateView):
    model = CustomUser
    template_name = 'registration/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('account:profile')
    success_message = 'حساب کاربری با موفقیت بروزرسانی شد'

    def get_object(self, queryset=None):
        return CustomUser.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user,
        })
        return kwargs
