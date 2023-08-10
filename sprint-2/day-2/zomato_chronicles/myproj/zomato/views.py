from django.shortcuts import render,redirect
import json
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from .models import Dish
def load_menu():
    menu_file_path = settings.BASE_DIR / 'zomato' / 'menu.json'
    try:
        with open(menu_file_path, 'r') as menu_file:
            return json.load(menu_file)
    except FileNotFoundError:
        return []

def save_menu(menu_data):
    menu_file_path = settings.BASE_DIR / 'zomato' / 'menu.json'
    with open(menu_file_path, 'w') as menu_file:
        json.dump(menu_data, menu_file, indent=4)

def load_orders():
    orders_file_path = settings.BASE_DIR / 'zomato' / 'orders.json'
    try:
        with open(orders_file_path, 'r') as orders_file:
            return json.load(orders_file)
    except FileNotFoundError:
        return []

def save_orders(orders):
    orders_file_path = settings.BASE_DIR / 'zomato' / 'orders.json'
    with open(orders_file_path, 'w') as orders_file:
        json.dump(orders, orders_file, indent=4)
        
def menu_view(request):
    menu_items = load_menu()

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add':
            dish_name = request.POST.get('dish_name')
            price = float(request.POST.get('price'))
            is_available = request.POST.get('is_available') == 'on'

            new_dish = {
                'dish_id': len(menu_items) + 1,
                'dish_name': dish_name,
                'price': price,
                'availability': is_available
            }

            menu_items.append(new_dish)
            save_menu(menu_items)

        elif action == 'delete':
            dish_id = int(request.POST.get('dish_id'))
            menu_items = [dish for dish in menu_items if dish['dish_id'] != dish_id]
            save_menu(menu_items)

    return render(request, 'menu/menu_list.html', {'menu_items': menu_items})


@csrf_exempt
def add_dish_view(request):
    if request.method == 'POST':
        dish_name = request.POST.get('dish_name')
        price = float(request.POST.get('price'))
        is_available = request.POST.get('is_available') == 'on'

        new_dish = {
            'dish_id': len(load_menu()) + 1,
            'dish_name': dish_name,
            'price': price,
            'availability': is_available
        }

        menu_data = load_menu()
        menu_data.append(new_dish)
        save_menu(menu_data)

        return redirect('menu_view')

    return render(request, 'menu/add_dish.html')


@csrf_exempt
def take_order_view(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        selected_dishes = request.POST.getlist('selected_dishes')

        # Retrieve menu data and filter selected dishes
        menu_items = Dish.all()
        ordered_dishes = [item for item in menu_items if str(item.dish_id) in selected_dishes]

        # Create an order dictionary and add it to the orders list
        new_order = {
            'customer_name': customer_name,
            'dishes': [{'dish_name': dish.dish_name, 'price': dish.price} for dish in ordered_dishes],
            'status': 'ordered'
        }
        orders = load_orders()
        orders.append(new_order)
        save_orders(orders)

        return redirect('menu_view')

    menu_items = Dish.all()
    return render(request, 'menu/take_order.html', {'menu_items': menu_items})

def orders_view(request):
    orders = load_orders()
    return render(request, 'menu/orders_list.html', {'orders': orders})

def update_order_status_view(request, order_index):
    orders = load_orders()

    if request.method == 'POST':
        new_status = request.POST.get('new_status')

        if order_index < len(orders):
            orders[order_index]['status'] = new_status
            save_orders(orders)

        return redirect('orders_view')

    current_status = orders[order_index]['status']
    return render(request, 'menu/update_order_status.html', {'order_index': order_index, 'current_status': current_status})


def delete_dish_view(request, dish_id):
    if request.method == 'POST':
        menu_items = load_menu()
        menu_items = [dish for dish in menu_items if dish['dish_id'] != dish_id]
        save_menu(menu_items)
    return redirect('menu_view')