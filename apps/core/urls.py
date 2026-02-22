from django.urls import path
from . import views


urlpatterns = [
    path("",views.MainPageView.as_view(),name="main-page"),
    path("about/",views.MainPageView.as_view(template_name="main-pages/about.html"),name="main-page"),
    path("contact/",views.MainPageView.as_view(template_name="main-pages/contact.html"),name="main-page"),
]