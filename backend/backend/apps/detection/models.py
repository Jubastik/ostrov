from django.db import models


class Detection(models.Model):
    camp = models.ForeignKey('camp.Camp', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
