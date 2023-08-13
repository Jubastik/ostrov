from django.db import models


class Detection(models.Model):
    camp = models.ForeignKey('camp.Camp', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Детект {self.camp.name} {self.time}"

    class Meta:
        verbose_name = "Детект"
        verbose_name_plural = "Детекты"
