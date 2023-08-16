from rest_framework import serializers
from .models import PowerData

class PowerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerData
        fields = "__all__"
        