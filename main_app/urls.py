from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cameras/', views.cameras_index, name='index'),
    path('cameras/<int:camera_id>/', views.cameras_detail, name='detail'),
]