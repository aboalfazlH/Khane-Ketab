from django.views import generic
from .models import Race,Question,Ask


class RaceListView(generic.ListView):
    model = Race
    context_object_name = "races"
    template_name = "race/races.html"