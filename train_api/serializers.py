from rest_framework import serializers
from train.models import Train


class TrainSerializer(serializers.ModelSerializer):
    departure_city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    arrival_city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Train
        exclude = []
