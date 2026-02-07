from django.views import generic
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "accounts/registration/register.html"
    success_url = reverse_lazy("main-page")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response