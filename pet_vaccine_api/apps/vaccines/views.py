from rest_framework.viewsets import ModelViewSet
from .models import Vaccine
from .serializers import VaccineSerializer


class VaccineViewSet(ModelViewSet):
    queryset = Vaccine.objects.all().order_by("-id")
    serializer_class = VaccineSerializer
