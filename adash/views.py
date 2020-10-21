from django.shortcuts import render,redirect
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from ad.models import *
from django.contrib.auth.models import User


# Create your views here.



# class index(ListView):
#   model = Ad
#  # query_set = Ad.objects.get.all().User.objects.filter(is_superuser=True)
#   query_set = Ad.objects.all().User.objects.filter(is_superuser='True')
#   #queryset = User.objects.get(permissions='is_superuser')
#   template_name = 'adash/index.html'





def Index(request):
  ads = Ad.objects.all()
  user = User
  user = request.user
  context = {'ads':ads}
  if user.is_staff == True:
   return render(request,'adash/index.html',context)
  else:
    return redirect('home')

 


""" def Home(request):
  if User.is_supruser:
    ads = Ad.objects.all()
    context = {'ads':ads}
  else:
     return redirect('login')
  return render(request,'adash/index.html',context)
 """
  

