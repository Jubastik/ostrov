from django.db import models


class Weather(models.Model):
    camp = models.ForeignKey('camp.Camp', on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Погода {self.camp.name} {self.time}"

    class Meta:
        verbose_name = "Погода"
        verbose_name_plural = "Погода"
