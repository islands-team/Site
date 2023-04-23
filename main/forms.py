from .models import User
from django.forms import ModelForm, TextInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['ima', 'familia', 'pochta', 'password']

        widgets = {
            "ima": TextInput(attrs={
                'class': 'name_input'
            }),
            "familia": TextInput(attrs={
                'class': 'fam_input'
            }),
            "pochta": TextInput(attrs={
                'class': 'mail_input'
            }),
            "password": TextInput(attrs={
                'class': 'password_input'
            })
        }