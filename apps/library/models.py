from django.db import models
from django.core.validators import FileExtensionValidator
from apps.accounts.models import CustomUser

class Book(models.Model):
    name = models.CharField(verbose_name="نام کتاب",max_length=110)
    description = models.TextField(verbose_name="توضیحات کتاب",blank=True,null=True)
    summary = models.TextField(verbose_name="خلاصه کتاب",blank=True,null=True)
    
    book_image = models.ImageField(verbose_name="تصویر کتاب",blank=True,null=True)
    
    preview = models.FileField(verbose_name="پیش نمایش صفحات کتاب",validators=[FileExtensionValidator(allowed_extensions=["pdf"])],blank=True,null=True)

    price = models.PositiveIntegerField(verbose_name="قیمت")

    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name="نویسنده")