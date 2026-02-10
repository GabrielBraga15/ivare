from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pet_vaccine_api.apps.users.views import ResponsibleViewSet
from pet_vaccine_api.apps.pets.views import PetViewSet
from pet_vaccine_api.apps.vaccines.views import VaccineViewSet
from pet_vaccine_api.apps.vaccinations.views import VaccinationViewSet


router = DefaultRouter()
router.register(r"responsibles", ResponsibleViewSet, basename="responsibles")
router.register(r"pets", PetViewSet, basename="pets")
router.register(r"vaccines", VaccineViewSet, basename="vaccines")
router.register(r"vaccinations", VaccinationViewSet, basename="vaccinations")
from django.http import JsonResponse


def home(_request):
    return JsonResponse({"status": "ok", "docs": "/api/"})


urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
