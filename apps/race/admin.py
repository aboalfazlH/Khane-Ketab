from django.contrib import admin
from .models import Race,Question,Ask

@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    filter_horizontal =("books",)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Ask)
class AskAdmin(admin.ModelAdmin):
    list_display = ("user",
                    "question",
                    "user_guess",
                    "ask_is_true")