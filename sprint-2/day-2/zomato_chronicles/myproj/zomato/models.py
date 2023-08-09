from django.db import models

# Create your models here.

import json
from django.conf import settings

def load_menu():
    menu_file_path = settings.BASE_DIR / 'zomato' / 'menu.json'
    with open(menu_file_path, 'r') as menu_file:
        return json.load(menu_file)

class Dish:
    def __init__(self, dish_id, dish_name, price, availability):
        self.dish_id = dish_id
        self.dish_name = dish_name
        self.price = price
        self.availability = availability

    @classmethod
    def all(cls):
        menu_data = load_menu()
        return [cls(**item) for item in menu_data]
