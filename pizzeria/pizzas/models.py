from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pizza(models.Model):
    '''voici une pizza'''
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        '''retourne le nom de la pizza'''
        return self.name

class Topping(models.Model):
    pizza = models.ManyToManyField(Pizza)
    name = models.CharField(max_length=50)
    field_name = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True)

    def __str__(self) -> str:
        return self.name

class Pizza_Comment(models.Model):
    '''Commentaires sur une pizza'''
    title = models.CharField(max_length=50)
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

