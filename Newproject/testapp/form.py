from django import forms
from django.contrib.auth.models import User

class CustmerForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password","email",]

    