from django.db import models
from django.core.validators import FileExtensionValidator
from apps.accounts.models import CustomUser

BooksType = [
    ("religious","مذهبی و دینی"),
    ("story","داستانی"),
    ("lesson","درسی"),
    ("comedy","کمدی"),
    ("war","جنگی"),
    ("autobiography","زندگی نامه"),
    ("romance","عاشقانه"),
    ("artistic","هنری"),
    ("travelogue","سفرنامه"),
    ("poetry","شعری"),
    ("historical","تاریخی"),
    ("political","سیاسی"),
]

Grades = [
    ("1","اول"),
    ("2","دوم"),
    ("3","سوم"),
    ("4","چهارم"),
    ("5","پنجم"),
    ("6","ششم"),
    ("7","هفتم"),
    ("8","هشتم"),
    ("9","نهم"),
    ("10","دهم"),
    ("11","یازدهم"),
    ("12","دوازدهم"),
    ("university","دانشگاه"),
    ("none","هیچکدام"),
]

class Book(models.Model):
    name = models.CharField(verbose_name="نام کتاب",max_length=110)
    description = models.TextField(verbose_name="توضیحات کتاب",blank=True,null=True)
    summary = models.TextField(verbose_name="خلاصه کتاب",blank=True,null=True)
    book_type = models.CharField(verbose_name="نوع کتاب",choices=BooksType,max_length=110)
    book_image = models.ImageField(verbose_name="تصویر کتاب",blank=True,null=True)
    is_verify = models.BooleanField(verbose_name="تائید شده(بررسی شده)",default=False)   
    is_active = models.BooleanField(verbose_name="فعال",default=False)   
    preview = models.FileField(verbose_name="پیش نمایش صفحات کتاب",validators=[FileExtensionValidator(allowed_extensions=["pdf"])],blank=True,null=True)

    price = models.PositiveIntegerField(verbose_name="قیمت",default=0)

    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name="نویسنده")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب ها"

class LibraryCard(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name="کاربر")
    grade = models.CharField(verbose_name="پایه تحصیلی",choices=Grades,max_length=110)
    city = models.CharField(verbose_name="شهر",max_length=110)
    age = models.PositiveSmallIntegerField(verbose_name="سن",)
    show_grade = models.BooleanField(verbose_name="نمایش پایه تحصیلی",default=True)
    show_city = models.BooleanField(verbose_name="نمایش شهر",default=True)
    show_age = models.BooleanField(verbose_name="نمایش سن",default=True)
    
    def __str__(self):
        return f"کارت کتابخانه ی {self.user}"