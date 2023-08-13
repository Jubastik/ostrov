from rest_framework import serializers

from backend.apps.camp.models import Camp, CampDetail, OtherPht


class OtherPhtSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherPht
        fields = '__all__'


class CampSerializer(serializers.ModelSerializer):
    occupied = serializers.BooleanField(read_only=True)
    temperature = serializers.FloatField(read_only=True)
    humidity = serializers.FloatField(read_only=True)
    pressure = serializers.FloatField(read_only=True)

    class Meta:
        model = Camp
        fields = '__all__'


class CampDetailSerializer(serializers.ModelSerializer):
    other_pht = OtherPhtSerializer(many=True, source='otherpht_set', read_only=True)


    class Meta:
        model = CampDetail
        fields = '__all__'
