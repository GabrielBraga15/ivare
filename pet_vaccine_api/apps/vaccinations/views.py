from rest_framework.viewsets import ModelViewSet
from .models import Vaccination
from .serializers import VaccinationSerializer


class VaccinationViewSet(ModelViewSet):
    queryset = (
        Vaccination.objects.select_related("pet", "vaccine").all().order_by("-id")
    )
    serializer_class = VaccinationSerializer
