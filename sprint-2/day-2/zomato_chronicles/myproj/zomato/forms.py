from django import forms

class AddDishForm(forms.Form):
    dish_name = forms.CharField(label='Dish Name', max_length=100)
    price = forms.DecimalField(label='Price', decimal_places=2)
    is_available = forms.BooleanField(label='Is Available', required=False)
