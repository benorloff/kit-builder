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
    # image = models.FileField(upload_to='images/cameras/%Y/%m/%d/')
    def __str__(self):
        return (f"{self.make} {self.model}")

class Lens(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=100)
    lens_type = models.CharField(max_length=30)
    focal_length = models.CharField(max_length=30)
    image_stab = models.BooleanField()
    mount = models.CharField(max_length=30)
    max_aperature = models.CharField(max_length=10)
    min_aperature = models.CharField(max_length=10)
    # image = models.FileField(upload_to='images/lenses/%Y/%m/%d/')
    def __str__(self):
        return (f"{self.make} {self.model}")
