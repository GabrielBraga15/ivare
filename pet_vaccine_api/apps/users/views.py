from rest_framework.viewsets import ModelViewSet
from .models import Responsible
from .serializers import ResponsibleSerializer


class ResponsibleViewSet(ModelViewSet):
    queryset = Responsible.objects.all().order_by("-id")
    serializer_class = ResponsibleSerializer
