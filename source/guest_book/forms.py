from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets


class BookForm(forms.Form):
    author = forms.CharField(max_length=30, required=True, label='Имя',
                             widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(max_length=254, required=True, label='Email',
                             widget=widgets.TextInput(attrs={'placeholder': 'Email Address'}))
    text = forms.CharField(max_length=1024, required=True, label='Текст', widget=widgets.Textarea)

    def cleaned_author(self):
        author = self.cleaned_data.get('author')
        if len(author) < 3:
            raise ValidationError('Имя должно быть длиннее 3 символов')
        return author

    def cleaned_email(self):
        email = self.cleaned_data.get('email')
        if len(email) < 3:
            raise ValidationError('Email должен быть длиннее 3 символов')
        return email

    def cleaned_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 5:
            raise ValidationError('Текст должен быть длиннее 5 символов')
        return text
