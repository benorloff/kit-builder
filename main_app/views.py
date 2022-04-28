from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import NewUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid
import boto3

from .models import Kit, Camera, Lens

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'kit-builder-app'

def home(request):
    return HttpResponse('<h1>Welcome to KitBuilder!</h1>')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('main_app:home')
        else:
            messages.error(request, "Invalid sign up - try again.")
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def about(request):
    return render(request, 'about.html')

class KitList(ListView):
    model = Kit
    def get_queryset(self):
        return Kit.objects.filter(user=self.request.user)

class KitCreate(CreateView):
    model = Kit
    fields = ['name']
    success_url = '/kits/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def kits_detail(request, kit_id):
    kit = Kit.objects.get(id=kit_id)
    cameras_kit_doesnt_have = Camera.objects.exclude(id__in = kit.cameras.all().values_list('id'))
    lenses_kit_doesnt_have = Lens.objects.exclude(id__in = kit.lenses.all().values_list('id'))
    return render(request, 'main_app/kit_detail.html', {
        'kit': kit,
        'cameras': cameras_kit_doesnt_have,
        'lenses': lenses_kit_doesnt_have,
    })

def assoc_camera(request, kit_id, camera_id):
    Kit.objects.get(id=kit_id).cameras.add(camera_id)
    return redirect('main_app:kits_detail', kit_id=kit_id)

def assoc_lens(request, kit_id, lens_id):
    Kit.objects.get(id=kit_id).lenses.add(lens_id)
    return redirect('main_app:kits_detail', kit_id=kit_id)

def unassoc_camera(request, kit_id, camera_id):
    Kit.objects.get(id=kit_id).cameras.remove(camera_id)
    return redirect('main_app:kits_detail', kit_id=kit_id)

def unassoc_lens(request, kit_id, lens_id):
    Kit.objects.get(id=kit_id).lenses.remove(lens_id)
    return redirect('main_app:kits_detail', kit_id=kit_id)

class KitUpdate(UpdateView):
    model = Kit
    fields = ['name']

class KitDelete(DeleteView):
    model = Kit
    success_url = '/kits/'

class CameraList(ListView):
    model = Camera
    
    def get_queryset(self):
        return Camera.objects.filter(user=self.request.user)

class CameraCreate(CreateView):
    model = Camera
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CameraDetail(DetailView):
    model = Camera

class CameraUpdate(UpdateView):
    model = Camera
    fields = '__all__'
    # def get_initial(self):
    #     print (self.object.__dict__)
    #     initial = super().get_initial()
    #     initial['make'] = self.object.make
    #     return initial

class CameraDelete(DeleteView):
    model = Camera
    success_url = '/cameras/'

class LensList(ListView):
    model = Lens

    def get_queryset(self):
        return Lens.objects.filter(user=self.request.user)

class LensCreate(CreateView):
    model = Lens
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class LensDetail(DetailView):
    model = Lens

class LensUpdate(UpdateView):
    model = Lens
    fields = '__all__'

class LensDelete(DeleteView):
    model = Lens
    success_url = '/lenses/'
