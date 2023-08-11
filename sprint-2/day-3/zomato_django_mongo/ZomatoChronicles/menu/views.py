from django.shortcuts import render,redirect
from .models import Dish
from .forms import AddDishForm

def menu_view(request):
    dishes = Dish.objects.all()
    return render(request, 'menu/menu.html', {'dishes': dishes})

def add_dish_view(request):
    if request.method == 'POST':
        form = AddDishForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the MongoDB database
            return redirect('menu')  # Redirect to the menu page after successful submission
    else:
        form = AddDishForm()
    return render(request, 'menu/add_dish.html', {'form': form})