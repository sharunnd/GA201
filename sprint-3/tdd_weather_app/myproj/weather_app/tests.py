from django.test import TestCase
import json
# Create your tests here.
from django.urls import reverse

class WeatherViewTest(TestCase):

    def test_can_access_weather_endpoint(self):
        response = self.client.get(reverse('weather', kwargs={'city': 'San Francisco'}))
        self.assertEqual(response.status_code,200)
    
    def test_invalid_city_returns_404(self):
        response = self.client.get(reverse('weather', kwargs={'city': 'InvalidCity'}))
        self.assertEqual(response.status_code, 404)

    def test_create_new_weather_data(self):
        new_data = {'city': 'Chicago', 'temperature': 18, 'weather': 'Cloudy'}
        response = self.client.post(reverse('weather-create'), data=new_data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
    
    def test_update_weather_data(self):
        updated_data = {'temperature': 25, 'weather': 'Sunny'}
        response = self.client.put(reverse('weather-update', kwargs={'city': 'San Francisco'}), data=json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_delete_weather_data(self):
        response = self.client.delete(reverse('weather-delete', kwargs={'city': 'San Francisco'}))
        print(response.status_code)
        print(response.content)
        self.assertEqual(response.status_code, 200)

