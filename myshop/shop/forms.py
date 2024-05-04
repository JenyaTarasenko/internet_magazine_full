from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    """Форма контаката"""
    class Meta:
        model = Contact
        fields = ['email', 'phone']





