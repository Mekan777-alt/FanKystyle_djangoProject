from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['message', 'user_name', 'subject', 'email']

        widgets = {
            'message': forms.TextInput(attrs={
                'class': 'form-control w-100', 'name': 'message', 'id': 'message', 'type': 'text',
                'cols': '30', 'row': '9',
                'placeholder': 'Enter Message'
            }),
            'user_name': forms.TextInput(attrs={
                'class': 'form-control', 'name': 'name', 'id': 'user_name', 'type': 'text',
                'placeholder': 'Enter your name'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control', 'name': 'email', 'id': 'email', 'type': 'text',
                'placeholder': 'Enter email address'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control', 'name': 'subject', 'id': 'subject', 'type': 'text',
                'placeholder': 'Enter Subject'
            }),
        }
