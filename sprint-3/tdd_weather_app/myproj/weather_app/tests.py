from django.test import TestCase

# Create your tests here.
from django.urls import reverse

class WeatherViewTest(TestCase):

    def test_can_access_weather_endpoint(self):
        response = self.client.get(reverse('weather', kwargs={'city': 'San Francisco'}))
        self.assertEqual(response.status_code,200)
    
    def test_invalid_city_returns_404(self):
        response = self.client.get(reverse('weather', kwargs={'city': 'InvalidCity'}))
        self.assertEqual(response.status_code, 404)