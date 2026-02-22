from django.views.generic import TemplateView
from apps.accounts.models import CustomUser
from apps.library.models import Book,BooksType
from django.db.models import Count


class MainPageView(TemplateView):
    template_name="main-pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["famous_authors"] = (
            CustomUser.objects.filter().order_by("-rate")[:3]
        )
        context["book_types"] = BooksType
        return context