from django.shortcuts import render,redirect
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from . models import *
from django.urls import reverse_lazy


# Create your views here.
class Home(ListView):
  model = Ad
  template_name = 'ads/ads.html'
  context_object_name = 'ads'




class CreateAd(CreateView):
  model = Ad 
  fields = '__all__'
  template_name = 'ads/create.html'
  success_url = reverse_lazy('ads')





class AdDetail(DetailView):
    model = Ad
    template_name='ads/detial.html'