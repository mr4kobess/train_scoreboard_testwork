from rest_framework import serializers
from train.models import Train


class TrainSerializer(serializers.ModelSerializer):
    departure_city = serializers.StringRelatedField(source='departure_city.name')
    arrival_city = serializers.StringRelatedField(source='arrival_city.name')
    status = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Train
        exclude = []
