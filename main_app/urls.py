from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('about/', views.about, name='about'),
    path('cameras/', views.cameras_index, name='index'),
    path('cameras/<int:camera_id>/', views.cameras_detail, name='detail'),
    path('lenses/', views.lenses_index, name='index'),
    path('lenses/<int:lens_id>/', views.lenses_detail, name='detail'),
]