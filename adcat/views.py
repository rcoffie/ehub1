from django.shortcuts import render,redirect
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from ad.models import *

# Create your views here.



def MP3(request):
  ads = Ad.objects.filter(category='Audio & MP3')
  context = {'ads':ads}
  return render(request,'adcat/audio.html',context)



def Mobile(request):
  ads = Ad.objects.filter(category='Mobile Phones')
  context = {'ads':ads}
  return render(request,'adcat/mobile.html',context)



def Cameras(request):
  ads = Ad.objects.filter(category='Cameras & Camcorders')
  context = {'ads':ads}
  return render(request,'adcat/camera.html',context)




def Other(request):
  ads = Ad.objects.filter(category='Other Electronics')
  context = {'ads':ads}
  return render(request,'adcat/other.html',context)