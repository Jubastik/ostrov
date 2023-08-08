from rest_framework import generics

from backend.apps.weather.models import Weather
from backend.apps.weather.serializers import WeatherSerializer


class WeatherAPIList(generics.ListCreateAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
