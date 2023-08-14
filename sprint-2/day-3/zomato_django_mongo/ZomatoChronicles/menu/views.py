from django.shortcuts import render,redirect,get_object_or_404
from .models import Dish,Order
from .forms import DishForm, OrderForm
import uuid
from django.views.decorators.http import require_POST

def generate_unique_id():
    return uuid.uuid4().int & (1<<31)-1
def home(request):
    dishes = Dish.objects.all()
    return render(request, 'menu/home.html', {'dishes': dishes})



def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            new_dish = form.save(commit=False)
            new_dish.dish_id = generate_unique_id()
            new_dish.save()
            return redirect('home')
    else:
        form = DishForm()
    return render(request, 'menu/add_dish.html', {'form': form})

def take_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.order_id = generate_unique_id()  # Manually generate order ID
            order.save()
            form.save_m2m()  # Save ordered items
            return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'menu/take_order.html', {'form': form})

@require_POST
def change_availability(request, dish_id):
    print("request method:<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<>>>>>>>>",request.method)
    try:
        dish = Dish.objects.get(pk=dish_id)
        # dish.availability = True  # Toggle availability
        # dish.save()
    except Dish.DoesNotExist:
        pass  # Handle dish not found

    return redirect('home')

def delete_dish(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    dish.delete()
    return redirect('home')

def orders(request):
    orders = Order.objects.all()
    return render(request, 'menu/orders.html', {'orders': orders})

def update_delivery_status(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    
    if order.order_status == 'delivered':
        order.order_status = 'received'
    else:
        order.order_status = 'delivered'
        
    order.save()
    return redirect('orders')