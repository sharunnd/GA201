from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu'),
    path('add_dish/', views.add_dish_view, name='add_dish_view'),
]
 