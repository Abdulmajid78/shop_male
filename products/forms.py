from django import forms
from .models import ProductColorModel


class ColorForm(forms.ModelForm):
    code = forms.CharField(max_length=7, widget=forms.TextInput(attrs={
        'type': 'color'
    }))

    class Meta:
        model = ProductColorModel
        fields = ['code']
