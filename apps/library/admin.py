from django.contrib import admin
from .models import Book,LibraryCard


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name","price","author",)

@admin.register(LibraryCard)
class LibraryCardAdmin(admin.ModelAdmin):
    pass