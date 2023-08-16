from django.urls import path,include
from . import views

urlpatterns = [
    path('weather/<str:city>/', views.weather_view, name='weather'),
]