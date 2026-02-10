from django.db import models


class Vaccine(models.Model):
    name = models.CharField(max_length=120, unique=True)
    manufacturer = models.CharField(max_length=120, blank=True)
    validity_months = models.PositiveIntegerField(default=12)

    def __str__(self):
        return self.name
