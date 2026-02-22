from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+[1-9]\d{1,14}$',
        message="تلفن همراه باید در قالب جهانی E.164 باشد (مثلاً +989123456789)."
    )

    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=15,
        unique=True,
        verbose_name="شماره موبایل",
        help_text="تلفن همراه باید در قالب جهانی E.164 باشد (مثلاً +989123456789)."
    )
    email = models.EmailField("آدرس ایمیل",unique=True,)
    avatar = models.ImageField("چهرک(اواتار)",blank=True,null=True)
    is_author = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(verbose_name="اعتبار نویسنده",default=0)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ("username","email")
    def __str__(self):
        full = self.get_full_name()
        return full if full else self.username
