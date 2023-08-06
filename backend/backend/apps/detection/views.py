from rest_framework import generics

from backend.apps.detection.models import Detection
from backend.apps.detection.serializers import DetectionSerializer


class DetectionAPIList(generics.ListCreateAPIView):
    queryset = Detection.objects.all()
    serializer_class = DetectionSerializer