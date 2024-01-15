from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, ProfileForm
from .models import CustomUser


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class Profile(generic.UpdateView):
    model = CustomUser
    template_name = 'registration/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('account:profile')

    def get_object(self, queryset=None):
        return CustomUser.objects.get(pk=self.request.user.pk)
