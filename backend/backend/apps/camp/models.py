from django.contrib.auth.models import User
from django.db import models
from datetime import timedelta

from django.utils import timezone

from backend.settings.dev import STATIC_URL


class Camp(models.Model):
    name = models.CharField(max_length=100)
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

    @property
    def occupied(self) -> bool:
        before = timezone.now() - timedelta(hours=4)
        detections = [i.time for i in self.detection_set.filter(time__range=[before, timezone.now()]).all()]
        return len(detections) > 6 or (len(detections) > 0 and max(detections).hour in range(22, 24))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Стоянка'
        verbose_name_plural = 'Стоянки'


class CampDetail(models.Model):
    camp = models.OneToOneField(Camp, on_delete=models.CASCADE, primary_key=True, verbose_name='Стоянка')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visibility = models.CharField(max_length=150, blank=True, verbose_name='Видимость с воды')
    ashore = models.CharField(max_length=150, blank=True, verbose_name='Тип берега')
    number_tents = models.IntegerField(blank=True, verbose_name='Мест для палаток')
    firewood = models.CharField(max_length=150, blank=True, verbose_name='Дрова')
    attractions = models.CharField(max_length=150, blank=True, verbose_name='Достопримечательности')
    conveniences = models.CharField(max_length=150, blank=True, verbose_name='Удобства')
    connection = models.CharField(max_length=150, blank=True, verbose_name='Связь')
    mosquitoes = models.CharField(max_length=150, blank=True, verbose_name='Комары/продуваемость')
    size = models.CharField(max_length=150, blank=True, verbose_name='Размер')
    sunset = models.CharField(max_length=150, blank=True, verbose_name='Закаты/рассветы')
    description = models.TextField(blank=True, verbose_name='Дополнительно')
    pht_from_water = models.ImageField(blank=True, upload_to=STATIC_URL, verbose_name='Фото с воды')
    pht_camping = models.ImageField(blank=True, upload_to=STATIC_URL, verbose_name='Фото стоянки')

    def __str__(self):
        return f"Детали стоянки {self.camp.name}"
    class Meta:
        verbose_name = 'Детали стоянки'
        verbose_name_plural = 'Детали стоянок'


class OtherPht(models.Model):
    image = models.ImageField(upload_to=STATIC_URL, verbose_name='Фото')
    camp_detail = models.ForeignKey(CampDetail, on_delete=models.CASCADE)

    def __str__(self):
        return f"Фото стоянки {self.camp_detail.camp.name}"
    class Meta:
        verbose_name = 'Дополнительное фото'
        verbose_name_plural = 'Дополнительные фото'
