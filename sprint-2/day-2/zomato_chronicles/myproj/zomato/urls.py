from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu_view, name='menu_view'),
    path('menu/order/', views.take_order_view, name='take_order_view'),
    path('menu/ordereditems/', views.orders_view, name='orders_view'),
    path('update_order_status/<int:order_index>/', views.update_order_status_view, name='update_order_status_view'),
    path('menu/add_dish/', views.add_dish_view, name='add_dish_view'),
    path('delete_dish/<int:dish_id>/', views.delete_dish_view, name='delete_dish_view'),
]
