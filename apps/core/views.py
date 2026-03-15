from django.views import generic
from apps.accounts.models import CustomUser
from apps.library.models import Book,BooksType
from django.db.models import Q
from django.shortcuts import render


class MainPageView(generic.TemplateView):
    
    template_name="main-pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["famous_authors"] = (
            CustomUser.objects.all().order_by("-rate")[:3]
        )
        context["exquisite_books"] = Book.objects.all().order_by("-rate")[:3]
        context["top_selling_books"] = Book.get_top_selling_books(3)
        context["book_types"] = BooksType
        return context


class SearchView(generic.View):
    
    def get(self,request,*args,**kwargs):
        context = self.get_context_data()
        return render(request,"search-results.html",context=context)
    
    def get_context_data(self):
        query = self.request.GET.get("q")
        context = {}
        for type in BooksType:
                context[type[0]]=Book.objects.filter(
                    Q(name__icontains=query)
                    |Q(summary__icontains=query)
                    |Q(description__icontains=query),
                    book_type=type[0]
                    )
        print(context)
        return context