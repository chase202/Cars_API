from rest_framework import serializers
from .models import Car

class Carserializer(serializers.modelserializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'price']