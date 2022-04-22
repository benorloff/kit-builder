from django.shortcuts import render
from django.http import HttpResponse

from .models import Camera

def home(request):
    return HttpResponse('<h1>Welcome to KitBuilder!</h1>')

def about(request):
    return render(request, 'about.html')

def cameras_index(request):
    return render(request, 'cameras/index.html', { 'cameras': cameras })
