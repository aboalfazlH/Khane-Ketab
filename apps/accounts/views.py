from django.shortcuts import render,redirect
from django.views import generic
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,mixins


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "accounts/registration/register.html"
    success_url = reverse_lazy("main-page")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class LoginView(generic.FormView):
    form_class = AuthenticationForm
    template_name = "accounts/registration/register.html"
    success_url = reverse_lazy("main-page")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class LogoutView(generic.View,mixins.LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        return render("accounts/registration/logout.html")
    
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect("accounts:main-page")