from django import forms
from .models import Dish

class AddDishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'price', 'availability']
