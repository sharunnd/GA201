from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.create_view, name='create_view'), 
    path('',views.read_view, name = 'read_view'),
    path('update/<str:name>',views.update_view, name = 'update_view'),
    path('delete/<str:name>/', views.delete_view, name='delete_view'),

] 