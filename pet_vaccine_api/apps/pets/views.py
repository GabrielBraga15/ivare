from rest_framework.viewsets import ModelViewSet
from .models import Pet
from .serializers import PetSerializer


class PetViewSet(ModelViewSet):
    queryset = Pet.objects.select_related("responsible").all().order_by("-id")
    serializer_class = PetSerializer
