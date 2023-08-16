from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .data import weather_data  

def weather_view(request, city):
    city_data = weather_data.get(city)
    if city_data is not None:
        return JsonResponse(city_data)
    else:
        return JsonResponse({'error': 'City not found'}, status=404)
