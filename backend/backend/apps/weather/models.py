from django.db import models


class Weather(models.Model):
    camp = models.ForeignKey('camp.Camp', on_delete=models.CASCADE)
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    pressure = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
