from django.shortcuts import render,redirect
from django.views import generic
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,mixins
from .models import CustomUser
from apps.library.models import LibraryCard

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "accounts/registration/register.html"
    success_url = reverse_lazy("create-library-card")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class LoginView(generic.FormView):
    
    form_class = AuthenticationForm
    template_name = "accounts/registration/register.html"
    success_url = reverse_lazy("main-page")
    
    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)
class LogoutView(generic.View,mixins.LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        return render(request,"accounts/registration/logout.html")
    
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect("main-page")

class UserPannelView(generic.DetailView):
    model = CustomUser
    template_name = "accounts/registration/pannel.html"
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["library_card"]= LibraryCard.objects.get(user=self.object)
        return context