from django.urls import path
from . import views

urlpatterns = [
    path("list/",views.BookListView.as_view(),name="book-list"),
    path("write/",views.BookCreateView.as_view(),name="book-write"),
    path("card/generate/",views.LibraryCardGenerateView.as_view(),name="create-library-card")
]