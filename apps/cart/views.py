from django.views import generic
from .models import BuyBook,Cart
from apps.library.models import Book
from django.shortcuts import redirect,render
from django.contrib.auth.mixins import LoginRequiredMixin


class AddBookToCartView(LoginRequiredMixin,generic.View):
    def get(self, request, book_id, *args, **kwargs):
        return self.add_to_cart(request, book_id=book_id,back_to_cart=True)

    def post(self, request, *args, **kwargs):
        book_id = request.POST.get("id")
        if not book_id:
            return redirect("main-page")
        return self.add_to_cart(request, book_id=book_id,back_to_cart=False)

    def add_to_cart(self, request, book_id,back_to_cart):
        book = Book.objects.get(id=book_id)

        cart_obj, created_cart = Cart.objects.get_or_create(user=request.user)

        buy_book_instance, created_buy_book = BuyBook.objects.get_or_create(
            book=book,
            cart=cart_obj,
            complete=False
        )

        
        if not created_buy_book:
            buy_book_instance.count += 1
            buy_book_instance.save()
        
        if back_to_cart:
            return redirect("cart-detail")
        else:
            return redirect("/")

class CartDetailView(generic.ListView):
    model = BuyBook
    template_name = "cart/detail.html"
    context_object_name = "books"
    def get_queryset(self):
        return BuyBook.objects.filter(cart__user=self.request.user,complete=False)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart"] = Cart.objects.get(user=self.request.user)
        return context

class CompleteBuyView(generic.View):
    def get(self, request, *args, **kwargs):

        return render(request,"cart/complete.html")
    
    def post(self, request, *args, **kwargs):
        cart = BuyBook.objects.filter(cart__user=request.user,complete=False)
        for book in cart:
            book.complete=True
            book.save()
        return redirect("cart-detail")