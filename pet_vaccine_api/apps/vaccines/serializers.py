from rest_framework import serializers
from .models import Vaccine


class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = ["id", "name", "manufacturer", "validity_months"]
