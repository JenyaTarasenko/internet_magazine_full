from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import CreateView
from .models import Contact

class ContactView(CreateView):
    """Форма контакта"""
    model = Contact
    form_class = ContactForm
    #перенаправляем на главную 
    success_url = '/'
    template_name ='contact/tags/form.html'
    
    
