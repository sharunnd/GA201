from django.db import models

# Create your models here.

class Dish(models.Model):
    dish_id = models.IntegerField(primary_key=True)
    dish_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.dish_name

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    ordered_items = models.ManyToManyField(Dish)
    order_status = models.CharField(max_length=100, default='received')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.customer_name}"


