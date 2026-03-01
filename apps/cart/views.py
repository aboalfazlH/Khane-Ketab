from django.views import generic
from .models import BuyBook,Cart
from apps.library.models import Book
from django.shortcuts import redirect


class AddBookToCartView(generic.View):
    def get(self, request, book_id, *args, **kwargs):
        return self.add_to_cart(request, book_id=book_id)

    def post(self, request, *args, **kwargs):
        book_id = request.POST.get("id")
        if not book_id:
            return redirect("main-page")
        return self.add_to_cart(request, book_id=book_id)

    def add_to_cart(self, request, book_id):
        book = Book.objects.get(id=book_id)

        cart_obj, created_cart = Cart.objects.get_or_create(user=request.user)

        buy_book_instance, created_buy_book = BuyBook.objects.get_or_create(
            book=book,
            cart=cart_obj,
        )

        
        if not created_buy_book:
            buy_book_instance.count += 1
            buy_book_instance.save()
        

        return redirect("main-page")

class CartDetailView(generic.ListView):
    model = BuyBook
    template_name = "cart/detail.html"
    context_object_name = "books"

    def get_queryset(self):
        return BuyBook.objects.filter(cart__user=self.request.user)