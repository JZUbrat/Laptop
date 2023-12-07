from rest_framework import serializers
from .models import Laptop

class Serializers(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'

        def create(self, validated_data):
            return Laptop.objects.create(**validated_data)