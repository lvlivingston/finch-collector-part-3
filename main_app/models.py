from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=50)
    scientificname = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    mass = models.CharField(max_length=10)
    diet = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
