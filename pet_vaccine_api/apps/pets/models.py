from django.db import models


class Pet(models.Model):
    SPECIES_CHOICES = [
        ("DOG", "Dog"),
        ("CAT", "Cat"),
        ("BIRD", "Bird"),
        ("OTHER", "Other"),
    ]

    name = models.CharField(max_length=120)
    species = models.CharField(max_length=10, choices=SPECIES_CHOICES)
    breed = models.CharField(max_length=120, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    responsible = models.ForeignKey(
        "users.Responsible", on_delete=models.CASCADE, related_name="pets"
    )

    def __str__(self):
        return self.name
