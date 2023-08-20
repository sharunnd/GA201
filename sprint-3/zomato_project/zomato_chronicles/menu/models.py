from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Dish(models.Model):
    dish_id = models.AutoField(primary_key=True)
    dish_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='dishes_added')
    customers_favorite = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='favorite_dishes')

    def __str__(self):
        return self.dish_name
    
class User(AbstractUser):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('customer', 'Customer'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    groups = None  # Set this to None to avoid reverse accessor clashes
    user_permissions = None  # Set this to None to avoid reverse accessor clashes