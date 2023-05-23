from django import forms
from .models import ContactMessageModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessageModel
        exclude = ['created_at']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'email'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'message'
            }),
        }
