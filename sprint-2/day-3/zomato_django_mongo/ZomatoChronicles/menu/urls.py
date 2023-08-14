from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('add_dish/', views.add_dish, name='add_dish'),
     path('take_order/', views.take_order, name='take_order'),
     path('change_availability/<int:dish_id>/', views.change_availability, name='change_availability'),
     path('delete_dish/<int:dish_id>/', views.delete_dish, name='delete_dish'),
     path('orders/', views.orders, name='orders'),
     path('update_delivery_status/<int:order_id>/', views.update_delivery_status, name='update_delivery_status'),
]
 