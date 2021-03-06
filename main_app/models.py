from django.db import models
from django.urls import reverse
from datetime import date

from django.contrib.auth.models import User

CAMERA_MAKE_CHOICES = (
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
)

class Camera(models.Model):
    make = models.CharField(max_length=255, choices=CAMERA_MAKE_CHOICES, default=CAMERA_MAKE_CHOICES[0][0])
    model = models.CharField(max_length=255)
    body_type = models.CharField(max_length=255)
    lens_mount = models.CharField(max_length=255)
    sensor_size = models.CharField(max_length=255)
    sensor_mp = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # image = models.FileField(upload_to='images/cameras/%Y/%m/%d/')
    def __str__(self):
        return (f"{self.make} {self.model}")
    def get_absolute_url(self):
        return reverse('main_app:cameras_detail', kwargs={'pk': self.id})
    def get_default(self):
        return self.make

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return (f"{self.name}")
    def get_absolute_url(self):
        return reverse('main_app:kits_detail', kwargs={'pk': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    lens = models.ForeignKey(Lens, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo @{self.url}"
