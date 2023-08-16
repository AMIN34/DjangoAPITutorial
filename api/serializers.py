from rest_framework import serializers
from .models import PowerData, File

class PowerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerData
        fields = "__all__"

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"