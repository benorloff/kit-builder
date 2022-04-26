import datetime

from django.db import models
from django.utils import timezone

class Camera(models.Model):
    MAKE_CHOICES = [
        ('AGF', 'Agfa'),
        ('CAN', 'Canon'),
        ('CAS', 'Casio'),
        ('CON', 'Contax'),
        ('DXO', 'DxO Labs'),
        ('FUJ', 'Fujifilm'),
        ('HAS', 'Hasselblad'),
        ('KOD', 'Kodak'),
        ('MIN', 'Minolta'),
        ('KYO', 'Kyocera'),
        ('LEI', 'Leica'),
        ('NIK', 'Nikon'),
        ('OLY', 'Olympus'),
        ('PAN', 'Panasonic'),
        ('PEN', 'Pentax'),
        ('RIC', 'Ricoh'),
        ('SAM', 'Samsung'),
        ('SIG', 'Sigma'),
        ('SON', 'Sony'),
        ('ZEI', 'Zeiss'),
    ] 
    make = models.CharField(max_length=30, choices=MAKE_CHOICES)
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
    image_stab = models.BooleanField('Image Stabilized')
    mount = models.CharField(max_length=30)
    max_aperture = models.CharField(max_length=10)
    min_aperture = models.CharField(max_length=10)
    # image = models.FileField(upload_to='images/lenses/%Y/%m/%d/')
    def __str__(self):
        return (f"{self.make} {self.model}")

class Kit(models.Model):
    name = models.CharField(max_length=50)
    cameras = models.ManyToManyField(Camera)
    lenses = models.ManyToManyField(Lens)
    def __str__(self):
        return (f"{self.name}")
