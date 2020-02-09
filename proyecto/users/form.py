from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# Extendemos del original
class UserCreateForm(UserCreationForm):
    # Ahora el campo username es de tipo email y cambiamos su texto
    #username = forms.EmailField(label="Correo electrónico")

    class Meta:
        model = CustomUser
        fields = ["email", "password1", "password2"]