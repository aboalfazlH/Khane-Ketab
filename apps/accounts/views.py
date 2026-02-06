from django.views import generic
from .forms import SignUpForm
from django.urls import reverse_lazy

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "accounts/registration/register.html"
    success_url = reverse_lazy("main-page")

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)