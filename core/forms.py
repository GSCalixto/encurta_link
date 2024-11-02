#Arquivo que usa os modelos de "moderls.py" para criar o formulario
from django import forms
from .models import Links

class FormLinks(forms.ModelForm):
    class Meta:
        model= Links
        fields= '__all__'