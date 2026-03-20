from django.shortcuts import render,redirect
from django.views import generic
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UsernameField
from django import forms
from django.contrib.auth import login,logout,mixins
from .models import CustomUser
from apps.library.models import LibraryCard
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = UsernameField(label="",widget=forms.TextInput(attrs={"autofocus": True,"placeholder":"شماره همراه (+989012345678)"}))
    password = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password","placeholder":"رمز عبور"}),
    )

    def __init__(self, *args, request=None, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)
        self._user = None

    def clean(self):
        cleaned = super().clean()
        username = cleaned.get("username")
        password = cleaned.get("password")
        if username and password:
            user = authenticate(self.request, username=username, password=password)
            if user is None:
                raise forms.ValidationError("نام کاربری یا رمز عبور اشتباه است.")
            self._user = user
        return cleaned

    def get_user(self):
        return self._user

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "accounts/registration/register.html"
    success_url = reverse_lazy("create-library-card")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class LoginView(generic.FormView):
    
    form_class = LoginForm
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
    context_object_name = "profile"
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["library_card"]= LibraryCard.objects.get(user=self.object)
        return context

class Famous_Authors(generic.ListView):
    model = CustomUser
    template_name = "accounts/authors.html"
    context_object_name = "authors"

    def get_queryset(self):
        return CustomUser.objects.all().order_by("-rate")
