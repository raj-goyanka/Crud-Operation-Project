# Import some Important Classes and functions.
from django import forms
from django.forms import fields, widgets
from .models import User

# Creating Model Forms Using ModelForm Class.
class UserForm(forms.ModelForm):
    class Meta:
      model=User
      fields=('name','email','password')
      widgets={
      'name':forms.TextInput(attrs={'class':'form-control text-dark'}),
      'email':forms.EmailInput(attrs={'class':'form-control'}),
      'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),}