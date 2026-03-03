from django.urls import path
from . import views

urlpatterns = [
    path("",views.RaceListView.as_view(),name="race"),
    path("quiz/",views.QuizView.as_view(),name="quiz"),
]