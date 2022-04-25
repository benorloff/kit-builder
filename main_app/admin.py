from django.contrib import admin

from .models import Camera
from .models import Lens

# Register your models here.

admin.site.register(Camera)
admin.site.register(Lens)