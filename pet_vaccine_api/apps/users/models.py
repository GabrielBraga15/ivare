from django.db import models


class Responsible(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name
