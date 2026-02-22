from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser 
        fields = ("phone_number","email","username","password1","password2")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser 
        fields = ("__all__")

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("phone_number", "email", "username", "first_name", "last_name", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = None
            field.label = ''
            
            placeholder_text = field_name.replace('_', ' ').title()
            
            if field_name in [f.name for f in self.Meta.model._meta.get_fields()]:
                placeholder_text = self.Meta.model._meta.get_field(field_name).verbose_name
            
            if field_name == 'password1':
                placeholder_text = 'رمز عبور'
            elif field_name == 'password2':
                placeholder_text = 'تکرار رمز عبور'

            field.widget.attrs.update({
                'placeholder': placeholder_text,
                'class': 'form-control',
            })