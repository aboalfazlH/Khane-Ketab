from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser 
        fields = ("phone_number","email","username","password1","password2")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser 
        fields = ("__all__")
    