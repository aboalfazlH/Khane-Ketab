from django.db import models
from apps.library.models import Book
from apps.accounts.models import CustomUser


Options = [
    ("option_1","گزینه ی یک"),
    ("option_2","گزینه ی دو"),
    ("option_3","گزینه ی سه"),
    ("option_4","گزینه ی چهار"),
]

class Race(models.Model):
    title = models.CharField(verbose_name="موضوع",max_length=110)
    books = models.ManyToManyField(Book,related_name="races",verbose_name="کتاب ها")
    is_active = models.BooleanField(verbose_name="فعال",default=True)
    thumbnail = models.ImageField(verbose_name="تصویر",blank=True,null=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "مسابقه"
        verbose_name_plural = "مسابقه ها"
    
class Question(models.Model):
    race = models.ForeignKey(Race,on_delete=models.CASCADE,verbose_name="مسابقه")
    text = models.TextField(verbose_name="متن سوال",)
    question_number = models.PositiveSmallIntegerField(verbose_name="شماره ی سوال")
    option_1 = models.TextField(verbose_name="گزینه ی یک",)
    option_2 = models.TextField(verbose_name="گزینه ی دو",)
    option_3 = models.TextField(verbose_name="گزینه ی سه",)
    option_4 = models.TextField(verbose_name="گزینه ی چهار",)
    true_option = models.CharField(verbose_name="گزینه ی صحیح",choices=Options,max_length=200)
    def __str__(self):
        return f"سوال شماره ی {self.question_number} برای آزمون {self.race}"
    
    class Meta:
        verbose_name = "سوال"
        verbose_name_plural = "سوال ها"

class Ask(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name="کاربر")
    question = models.ForeignKey(Question,on_delete=models.CASCADE,verbose_name="سوال")
    user_guess = models.CharField(verbose_name="حدس کاربر",choices=Options,max_length=200,blank=True,null=True)

    @property
    def ask_is_true(self):
        return "✅" if self.user_guess == self.question.true_option else "❌"
    
    def __str__(self):
        return f"جواب {self.user} در آزمون {self.question.race} به سوال شماره ی {self.question.question_number}"
    
    class Meta:
        verbose_name = "پاسخ"
        verbose_name_plural = "پاسخ ها"
    