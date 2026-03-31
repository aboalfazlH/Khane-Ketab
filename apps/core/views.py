from django.views import generic
from apps.accounts.models import CustomUser
from apps.library.models import Book,BooksType
from django.db.models import Q
from django.shortcuts import render

num = None
BookTypes = list(BooksType)
for book_type in range(len(BookTypes)):
    i = book_type
    book_type = list(BooksType[book_type])
    match i+1:
        case 1:
            num="one"
        case 2:
            num="two"
        case 3:
            num="three"
        case 4:
            num="four"
        case 5:
            num="five"
        case 6:
            num="six"
        case 7:
            num="seven"
        case 8:
            num="eight"
        case 9:
            num="nine"
        case 10:
            num="ten"
        case 11:
            num="eleven"
        case 12:
            num="twelve"
    book_type.append(num)
    book_type = tuple(book_type)

    BookTypes[i]=book_type
    
class MainPageView(generic.TemplateView):    
    template_name="main-pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["famous_authors"] = (
            CustomUser.objects.all().order_by("-rate")[:3]
        )
        context["exquisite_books"] = Book.objects.all().order_by("-rate")[:3]
        context["top_selling_books"] = Book.get_top_selling_books(3)
        
        context["book_types"] = BookTypes
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