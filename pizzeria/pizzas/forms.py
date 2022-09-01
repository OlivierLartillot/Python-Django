from django import forms

from .models import Pizza, Topping

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        labels = {'Name': ''}

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['pizza','name']
        labels = {'pizza': 'A quelle Pizza', 'name': 'Nom'}

      