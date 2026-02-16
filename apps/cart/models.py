from django.db import models
from apps.library.models import Book,CustomUser

class Cart(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    @property
    def total_price(self):
        books_in_cart = self.buybook_set.all()
        total = sum(item.book.price for item in books_in_cart)
        return total

class BuyBook(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)