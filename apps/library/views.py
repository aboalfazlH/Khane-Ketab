from django.shortcuts import render
from django.views import generic
from .models import Book,LibraryCard
from .forms import LibraryCardForm
from django.urls import reverse_lazy
from .forms import BookForm

class BookListView(generic.ListView):
    model = Book
    model = Book
    context_object_name = "books"
    template_name = "library/book-list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.filter(is_verify=True,is_active=True)
        return context

class BookCreateView(generic.CreateView):
    form_class = BookForm
    template_name = "library/book-create.html"
    success_url = reverse_lazy("book-list")
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class LibraryCardGenerateView(generic.CreateView):
    model = LibraryCard
    form_class = LibraryCardForm
    template_name = "accounts/registration/register.html"
    success_url = reverse_lazy("main-page")
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)