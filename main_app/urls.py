from django.urls import path, include
from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('kits/', views.KitList.as_view(), name='kits_index'),
    path('kits/create/', views.KitCreate.as_view(), name='kits_create'),
    path('kits/<int:kit_id>/', views.kits_detail, name='kits_detail'),
    # path('kits/<int:kit_id>/add_photo/', views.add_photo, name='add_photo'),
    path('kits/<int:kit_id>/assoc_camera/<int:camera_id>/', views.assoc_camera, name='assoc_camera'),
    path('kits/<int:kit_id>/assoc_lens/<int:lens_id>/', views.assoc_lens, name='assoc_lens'),
    path('kits/<int:kit_id>/unassoc_camera/<int:camera_id>/', views.unassoc_camera, name='unassoc_camera'),
    path('kits/<int:kit_id>/unassoc_lens/<int:lens_id>/', views.unassoc_lens, name='unassoc_lens'),
    path('kits/<int:pk>/update/', views.KitUpdate.as_view(), name='kits_update'),
    path('kits/<int:pk>/delete/', views.KitDelete.as_view(), name='kits_delete'),
    path('cameras/', views.CameraList.as_view(), name='cameras_index'),
    path('cameras/create/', views.CameraCreate.as_view(), name='cameras_create'),
    path('cameras/<int:pk>/', views.CameraDetail.as_view(), name='cameras_detail'),
    path('cameras/<int:pk>/update/', views.CameraUpdate.as_view(), name='cameras_update'),
    path('cameras/<int:pk>/delete/', views.CameraDelete.as_view(), name='cameras_delete'),
    path('lenses/', views.LensList.as_view(), name='lenses_index'),
    path('lenses/create/', views.LensCreate.as_view(), name='lenses_create'),
    path('lenses/<int:pk>/', views.LensDetail.as_view(), name='lenses_detail'),
    path('lenses/<int:pk>/update/', views.LensUpdate.as_view(), name='lenses_update'),
    path('lenses/<int:pk>/delete/', views.LensDelete.as_view(), name='lenses_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]