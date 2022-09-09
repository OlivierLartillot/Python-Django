from dataclasses import field
from django import forms


from .models import Pizza, Topping, Pizza_Comment

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        labels = {'Name': ''}

class ToppingForm(forms.ModelForm):   


    pizza_choices = forms.ModelMultipleChoiceField(
    widget=forms.CheckboxSelectMultiple,
    queryset=Pizza.objects.all()
        )
    class Meta:
        model = Topping    
        fields = ['pizza', 'name']
        labels = {'pizza': 'A quelle Pizza', 'name': 'Nom'}

class PizzaCommentForm(forms.ModelForm):
    class Meta:
        model = Pizza_Comment
        fields = ['title','text']
        labels = {
                    'title': 'Titre de votre commentaire',
                     'text': 'Commentaire'
                }

      