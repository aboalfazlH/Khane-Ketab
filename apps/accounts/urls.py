from django.urls import path
from . import views


app_name = "accounts"
urlpatterns = [
    path("signup/",views.SignUpView.as_view(),name="signup"),
    path("login/",views.LoginView.as_view(),name="login"),
    path("logout/",views.LogoutView.as_view(),name="logout"),
    path("authors/",views.Famous_Authors.as_view(),name="authors"),
    path("<str:username>/",views.UserPannelView.as_view(),name="user-pannel"),
]