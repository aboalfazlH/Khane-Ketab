from django.urls import path
from . import views


urlpatterns = [
    path("me/",views.CartDetailView.as_view(),name="cart-detail"),
    path("<int:book_id>/",views.AddBookToCartView.as_view(),name="main-page"),
]