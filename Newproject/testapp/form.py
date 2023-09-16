from typing import Any, Dict
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from testapp.models import ContactUs,bookModel

class CustmerForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]
#Contatus Us
class ContactUs_Form(forms.ModelForm):
   
    class Meta:
        model=ContactUs
        fields="__all__"
    def clean(self):
        cleaned_data = super().clean()
        inputname = cleaned_data.get('username')
        

        if inputname:
            #perform username validation
            if len(inputname)<5:
                raise forms.ValidationError("Username must be longer than 5 characters.")

            for i in inputname:
                if not i.isalpha() and i !=" ":
                     raise forms.ValidationError("Username must contain only alphabetic characters and spaces.")
            
            #validating Email
            inputemail=cleaned_data.get("email")
            if inputemail:
                if not inputemail.endswith('@gmail.com'):
                    raise forms.ValidationError("Emial should conatin @gamil.com")


            #validating Comments
            inputcomments=cleaned_data.get("comments")
            if inputcomments:
                for i in inputcomments:
                    if not i.isalpha() and i !=" " and i != ",":
                        raise forms.ValidationError("Comments must contain only alphabetic characters and spaces.")


class BookForm(forms.ModelForm):
    class Meta:
        model = bookModel
        fields = "__all__"
        widgets = {
            'Booking_date': forms.DateInput(attrs={'type': 'date'})
        }


    