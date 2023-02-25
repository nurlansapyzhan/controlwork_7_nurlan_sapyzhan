from django import forms
from django.forms import widgets


class BookForm(forms.Form):
    author = forms.CharField(max_length=30, required=True, label='Имя',
                             widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(max_length=254, required=True, label='Email',
                             widget=widgets.TextInput(attrs={'placeholder': 'Email Address'}))
    text = forms.CharField(max_length=1024, required=True, label='Текст', widget=widgets.Textarea)
