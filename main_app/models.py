import datetime

from django.db import models
from django.urls import reverse
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
    make = models.CharField(max_length=255, choices=MAKE_CHOICES)
    model = models.CharField(max_length=255)
    body_type = models.CharField(max_length=255)
    lens_mount = models.CharField(max_length=255)
    sensor_size = models.CharField(max_length=255)
    sensor_mp = models.DecimalField(max_digits=5, decimal_places=2)
    # image = models.FileField(upload_to='images/cameras/%Y/%m/%d/')
    def __str__(self):
        return (f"{self.make} {self.model}")
    def get_absolute_url(self):
        return reverse('main_app:cameras_detail', kwargs={'pk': self.id})

class Lens(models.Model):
    MAKE_CHOICES = [
        ('BOW', 'Bower'),
        ('CAN', 'Canon'),
        ('IRI', 'Irix'),
        ('KOW', 'Kowa'),
        ('LEN', 'Lensbaby'),
        ('MEI', 'Meike'),
        ('MEY', 'Meyer-Optik Gorlitz'),
        ('MIT', 'Mitakon Zhongyi'),
        ('NIK', 'Nikon'),
        ('OPT', 'Opteka'),
        ('PEN', 'Pentax'),
        ('ROK', 'Rokinon'),
        ('SAM', 'Samyang'),
        ('SCH', 'Schneider'),
        ('SIG', 'Sigma'),
        ('SON', 'Sony'),
        ('TAM', 'Tamron'),
        ('TOK', 'Tokina'),
        ('VEN', 'Venus Optics'),
        ('VIV', 'Vivitar'),
        ('VOI', 'Voigtlander'),
        ('YON', 'Yongnuo'),
        ('ZEI', 'Zeiss'),
        ('ZEN', 'Zenit'),
    ]
    make = models.CharField(max_length=255, choices=MAKE_CHOICES)
    model = models.CharField(max_length=255)
    lens_type = models.CharField(max_length=255)
    focal_length = models.CharField(max_length=255)
    image_stab = models.BooleanField('Image Stabilized')
    mount = models.CharField(max_length=255)
    max_aperture = models.CharField(max_length=255)
    min_aperture = models.CharField(max_length=255)
    # image = models.FileField(upload_to='images/lenses/%Y/%m/%d/')
    class Meta:
        verbose_name_plural = 'lenses'
    def __str__(self):
        return (f"{self.make} {self.model}")
    def get_absolute_url(self):
        return reverse('main_app:lenses_detail', kwargs={'pk': self.id})

class Kit(models.Model):
    name = models.CharField(max_length=255)
    cameras = models.ManyToManyField(Camera)
    lenses = models.ManyToManyField(Lens)
    def __str__(self):
        return (f"{self.name}")
    def get_absolute_url(self):
        return reverse('main_app:kits_detail', kwargs={'pk': self.id})
