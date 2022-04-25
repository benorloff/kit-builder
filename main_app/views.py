from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .models import Camera, Lens

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

def cameras_index(request):
    cameras = Camera.objects.order_by('make')
    context = {'cameras': cameras}
    return render(request, 'cameras/index.html', context)

def cameras_detail(request, camera_id):
    camera = get_object_or_404(Camera, pk=camera_id)
    return render(request, 'cameras/detail.html', {'camera': camera})

def lenses_index(request):
    lenses = Lens.objects.order_by('make')
    context = {'lenses': lenses}
    return render(request, 'lenses/index.html', context)

def lenses_detail(request, lens_id):
    lens = get_object_or_404(Lens, pk=lens_id)
    return render(request, 'lenses/detail.html', {'lens': lens})
