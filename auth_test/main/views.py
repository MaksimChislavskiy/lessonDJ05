from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic  import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from urllib import request
from .forms import CustomUserCreationForm

class HomePageView(TemplateView):
    template_name = 'index.html'


class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    login_url = 'login'


class RegisterPageView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        self.object = form.save()
        login(self.request, self.object)
        return HttpResponseRedirect(self.get_success_url())


class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('profile')

    def get_success_url(self):
        return reverse_lazy('profile')
