from django.shortcuts import render
from django.http import HttpResponse

class Camera:  # Note that parens are optional if not inheriting from another class
  def __init__(self, make, model, body_type, lens_mount, sensor_size, sensor_mp = 0):
    self.make = make
    self.model = model
    self.body_type = body_type
    self.lens_mount = lens_mount
    self.sensor_size = sensor_size
    self.sensor_mp = sensor_mp

cameras = [
  Camera('Nikon', 'Z9', 'SLR-style mirrorless', 'Nikon Z', 'Full frame', 46),
  Camera('Leica', 'M11', 'Large SLR', 'Leica M', 'Full frame', 60),
  Camera('Sony', 'a7 IV', 'SLR-style mirrorless', 'Sony E', 'Full frame', 33),
  Camera('Fujifilm', 'GFX 100S', 'SLR-style mirrorless', 'Fujifilm G', 'Medium format', 102),
  Camera('Canon', 'EOS R3', 'SLR-style mirrorless', 'Canon RF', 'Full frame', 24),
]

def home(request):
    return HttpResponse('<h1>Welcome to KitBuilder!</h1>')

def about(request):
    return render(request, 'about.html')

def cameras_index(request):
    return render(request, 'cameras/index.html', { 'cameras': cameras })
