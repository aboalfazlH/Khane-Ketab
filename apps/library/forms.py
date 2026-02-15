from django import forms
from .models import LibraryCard,Book

class LibraryCardForm(forms.ModelForm):
    class Meta:
        model = LibraryCard
        fields = ("grade","city","age","show_grade","show_city","show_age",)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("name","description","summary","book_type","book_image","preview")