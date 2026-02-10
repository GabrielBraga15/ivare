from rest_framework import serializers
from .models import Responsible


class ResponsibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsible
        fields = ["id", "name", "email", "phone"]
