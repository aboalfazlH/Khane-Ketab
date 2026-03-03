from django.views import generic
from .models import Race,Question,Ask


class RaceListView(generic.ListView):
    model = Race
    context_object_name = "races"
    template_name = "race/races.html"

class QuizView(generic.View):
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        race_id = self.request.GET.get("id")
        race = Race.objects.get(id=race_id)
        context["race"] = race
        context["questions"] = Question.objects.filter(race=race)
        return context
    
    def form_valid(self, form):
        return super().form_valid(form)