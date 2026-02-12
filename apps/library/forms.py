from django import forms
from .models import LibraryCard

class LibraryCardForm(forms.ModelForm):
    class Meta:
        model = LibraryCard
        fields = ("grade","city","age","show_grade","show_city","show_age",)