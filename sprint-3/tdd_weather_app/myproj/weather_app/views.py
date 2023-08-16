from django.shortcuts import render
import json
# Create your views here.
from django.http import JsonResponse
from .data import weather_data  

def weather_view(request, city):
    city_data = weather_data.get(city)

    if city_data is not None:
        return JsonResponse(city_data)
    else:
        return JsonResponse({'error': 'City not found'}, status=404)

def create_weather(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        city = data.get('city')
        temperature = data.get('temperature')
        weather = data.get('weather')

        if city and temperature is not None and weather:
            weather_data[city] = {'temperature': temperature, 'weather': weather}
            return JsonResponse({'message': f'Weather data for {city} created successfully'}, status=201)
        else:
            return JsonResponse({'error': 'Invalid data'}, status=400)
        

def update_weather(request, city):
    if request.method == 'PUT':
        data = json.loads(request.body)
        temperature = data.get('temperature')
        weather = data.get('weather')

        if city in weather_data and (temperature is not None or weather is not None):
            if temperature is not None:
                weather_data[city]['temperature'] = temperature
            if weather is not None:
                weather_data[city]['weather'] = weather
            return JsonResponse(weather_data[city])
        else:
            return JsonResponse({'error': 'City not found or invalid data'}, status=404)

def delete_weather(request, city):
    if city in weather_data:
        del weather_data[city]
        return JsonResponse({'message': 'Weather data deleted successfully'}, status=204)
    else:
        return JsonResponse({'error': 'City not found'}, status=404)
