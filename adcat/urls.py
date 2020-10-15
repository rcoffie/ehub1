from django.urls import path
from . import views

urlpatterns = [
#path('',views.MP3,name='audio'),
path('audio/',views.MP3,name='audio'),
path('mobile/',views.Mobile,name='mobile'),
path('camera/',views.Cameras,name='camera'),
path('other/',views.Other,name='other')
]
