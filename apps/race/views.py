from django.views import generic
from .models import Race,Question,Ask,Options
from django.contrib import messages
from django.shortcuts import redirect,render


class RaceListView(generic.ListView):
    model = Race
    context_object_name = "races"
    template_name = "race/races.html"

class QuizView(generic.View):
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request,"race/quiz.html",context=context)
    
    def post(self, request, *args, **kwargs):
        race_id = self.request.POST.get("id")
        race = Race.objects.get(id=race_id)
        questions = race.question_set.all()
        
        for question in questions:
            user_guess = self.request.POST.get(f"{question.question_number}")
            a = Ask.objects.create(question=question,user=request.user,)
          
            match user_guess:
                case question.option_1:
                    a.user_guess = Options[0][0]
                case question.option_2:
                    a.user_guess = Options[1][0]
                case question.option_3:
                    a.user_guess = Options[2][0]
                case question.option_4:
                    a.user_guess = Options[3][0]
                case "":
                    print("هیچی به هیچی!")
            a.save()
        return redirect("main-page")
    
    def get_context_data(self, **kwargs):
        context = {}
        race_id = self.request.GET.get("id")
        race_ = Race.objects.get(id=race_id)
        if race_:
            context["race"] = race_
            context["questions"] = Question.objects.filter(race=race_).order_by("question_number")
        return context
    
    def form_valid(self, form):
        return super().form_valid(form)