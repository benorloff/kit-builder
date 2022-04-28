from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from .forms import NewUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .models import Kit, Camera, Lens

def home(request):
    return HttpResponse('<h1>Welcome to KitBuilder!</h1>')

def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('main_app:home')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, 'register.html', {'register_form': form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('main_app:home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('main_app:home')

def about(request):
    return render(request, 'about.html')

class KitList(ListView):
    model = Kit

class KitCreate(CreateView):
    model = Kit
    fields = ['name']
    success_url = '/kits/'

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

class KitUpdate(UpdateView):
    model = Kit
    fields = ['name']

class KitDelete(DeleteView):
    model = Kit
    success_url = '/kits/'

class CameraList(ListView):
    model = Camera

class CameraCreate(CreateView):
    model = Camera
    fields = '__all__'

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

class LensCreate(CreateView):
    model = Lens
    fields = '__all__'

class LensDetail(DetailView):
    model = Lens

class LensUpdate(UpdateView):
    model = Lens
    fields = '__all__'

class LensDelete(DeleteView):
    model = Lens
    success_url = '/lenses/'
