from django.db import models


class Vaccination(models.Model):
    pet = models.ForeignKey(
        "pets.Pet", on_delete=models.CASCADE, related_name="vaccinations"
    )
    vaccine = models.ForeignKey(
        "vaccines.Vaccine", on_delete=models.PROTECT, related_name="applications"
    )
    applied_at = models.DateField()
    veterinarian = models.CharField(max_length=120, blank=True)

    class Meta:
        unique_together = ("pet", "vaccine", "applied_at")

    def __str__(self):
        return f"{self.pet_id}-{self.vaccine_id}-{self.applied_at}"
