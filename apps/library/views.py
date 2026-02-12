from django.shortcuts import render
from django.views import generic
from .models import Book,LibraryCard
from .forms import LibraryCardForm
from django.urls import reverse_lazy

class BookListView(generic.ListView):
    model = Book
    context_object_name = "books"
    template_name = "library/book-list.html"

class LibraryCardGenerateView(generic.CreateView):
    model = LibraryCard
    form_class = LibraryCardForm
    template_name = "accounts/registration/register.html"
    success_url = reverse_lazy("main-page")
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)