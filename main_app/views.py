from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Camera

def home(request):
    return HttpResponse('<h1>Welcome to KitBuilder!</h1>')

def about(request):
    return render(request, 'about.html')

def cameras_index(request):
    cameras = Camera.objects.order_by('make')
    context = {'cameras': cameras}
    return render(request, 'cameras/index.html', context)

def cameras_detail(request, camera_id):
    camera = get_object_or_404(Camera, pk=camera_id)
    return render(request, 'cameras/detail.html', {'camera': camera})
