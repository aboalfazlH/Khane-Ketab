from django.db import models

class Cart(models.Model):
    user = models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE)
    @property
    def total_price(self):
        books_in_cart = self.buybook_set.all()
        total = sum(item.book.price for item in books_in_cart)
        return total
    
    def __str__(self):
        return f"سبد خرید {self.user}"

class BuyBook(models.Model):
    book = models.ForeignKey('library.Book',on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    count = models.PositiveSmallIntegerField(default=1)
    def __str__(self):
        return f"کتاب {self.book}"