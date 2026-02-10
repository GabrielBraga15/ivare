from rest_framework import serializers
from .models import Vaccination


class VaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccination
        fields = ["id", "pet", "vaccine", "applied_at", "veterinarian"]
