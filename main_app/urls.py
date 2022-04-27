from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('about/', views.about, name='about'),
    path('kits/', views.KitList.as_view(), name='kits_index'),
    path('kits/create/', views.KitCreate.as_view(), name='kits_create'),
    path('kits/<int:pk>/', views.KitDetail.as_view(), name='kits_detail'),
    path('kits/<int:pk>/update/', views.KitUpdate.as_view(), name='kits_update'),
    path('kits/<int:pk>/delete/', views.KitDelete.as_view(), name='kits_delete'),
    path('cameras/', views.CameraList.as_view(), name='cameras_index'),
    path('cameras/<int:camera_id>/', views.cameras_detail, name='detail'),
    path('cameras/<int:pk>/update/', views.CameraUpdate.as_view(), name='cameras_update'),
    path('cameras/<int:pk>/delete/', views.CameraDelete.as_view(), name='cameras_delete'),
    path('lenses/', views.lenses_index, name='index'),
    path('lenses/<int:lens_id>/', views.lenses_detail, name='detail'),
]