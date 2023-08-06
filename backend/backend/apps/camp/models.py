from django.contrib.auth.models import User
from django.db import models
from datetime import timedelta

from django.utils import timezone

from backend.settings.dev import STATIC_URL


class Camp(models.Model):
    name = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()

    @property
    def occupied(self) -> bool:
        before = timezone.now() - timedelta(hours=4)
        detections = [i.time for i in self.detection_set.filter(time__range=[before, timezone.now()]).all()]
        return len(detections) > 6 or (len(detections) > 0 and max(detections).hour in range(22, 24))


class CampDetail(models.Model):
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visibility = models.CharField(max_length=150, blank=True)
    ashore = models.CharField(max_length=150, blank=True)
    number_tents = models.IntegerField(blank=True)
    firewood = models.CharField(max_length=150, blank=True)
    conveniences = models.CharField(max_length=150, blank=True)
    connection = models.CharField(max_length=150, blank=True)
    mosquitoes = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    pht_from_water = models.ImageField(blank=True, upload_to=STATIC_URL)
    pht_camping = models.ImageField(blank=True, upload_to=STATIC_URL)


class OtherPht(models.Model):
    image = models.ImageField(upload_to=STATIC_URL)
    camp_detail = models.ForeignKey(CampDetail, on_delete=models.CASCADE)
