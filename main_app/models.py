import datetime

from django.db import models
from django.utils import timezone

class Camera(models.Model): 
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=50)
    body_type = models.CharField(max_length=50)
    lens_mount = models.CharField(max_length=50)
    sensor_size = models.CharField(max_length=50)
    sensor_mp = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.make, self.model
