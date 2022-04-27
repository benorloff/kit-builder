from django.contrib import admin

from .models import Kit, Camera, Lens

# Register your models here.

admin.site.register(Kit)
admin.site.register(Camera)
admin.site.register(Lens)