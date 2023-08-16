from django.urls import path,include
from . import views

urlpatterns = [
    path('weather/<str:city>/', views.weather_view, name='weather'),
    path('weather/', views.create_weather, name='weather-create'),
    path('weather/<str:city>/', views.update_weather, name='weather-update'),
    path('weather/<str:city>/', views.delete_weather, name='weather-delete'),

]