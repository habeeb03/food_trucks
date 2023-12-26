from rest_framework import serializers
from .models import Truck


class FoodTruckSerializer(serializers.ModelSerializer):
    distance = serializers.FloatField(read_only=True)

    class Meta:
        model = Truck
        fields = '__all__'
