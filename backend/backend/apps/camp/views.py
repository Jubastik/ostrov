from rest_framework import generics

from backend.apps.camp.models import Camp, CampDetail, OtherPht
from backend.apps.camp.serializers import CampSerializer, CampDetailSerializer, OtherPhtSerializer


class CampAPIList(generics.ListCreateAPIView):
    queryset = Camp.objects.all()
    serializer_class = CampSerializer


class CampAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Camp.objects.all()
    serializer_class = CampSerializer


class CampDetailAPIList(generics.ListCreateAPIView):
    queryset = CampDetail.objects.all()
    serializer_class = CampDetailSerializer


class CampDetailAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CampDetail.objects.all()
    serializer_class = CampDetailSerializer
    lookup_field = 'camp_id'


class OtherPhtAPIList(generics.ListCreateAPIView):
    queryset = OtherPht.objects.all()
    serializer_class = OtherPhtSerializer
