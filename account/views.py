from django.shortcuts import render,redirect 
from django.contrib import messages,auth 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from ad.models import *
from django.urls import reverse_lazy

# Create your views here.


def Login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request,user)
      messages.success(request, 'you are now loggined in ')
      return redirect('dashboard')
  return render(request,'account/login.html')




def Register(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email    = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      if User.objects.filter(username=username).exists():
        messages.error(request, 'username already exists')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'email already taken')
          return redirect('register')
        else:
          user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password,email=email)
          user.save()
          messages.success(request, 'Account Created Successfuly')
          return redirect('login')
    else:
      messages.error(request, 'Password do not match')
      return redirect('register')

  return render(request,'account/registration.html')



""" 
def Dashboard(request):
  return render(request,'account/dashboard.html') """


class Dashboard(ListView):
  model = Ad
  context_object_name = 'ads'

 
  template_name = 'account/dashboard.html'
  def get_queryset(self):
      return  Ad.objects.filter(seller=self.request.user)



class Dashboard_Detail(DetailView):
  model = Ad 
  template_name = 'account/d_detail.html'




class Dashboard_edit(UpdateView):
  model = Ad 
  fields  = ['title','location','region','category','condition','price','brand','negotiable','main_photo','photo_1','photo_2','photo_3','description']
  template_name = 'account/d_update.html'
  success_url = reverse_lazy('dashboard')

    
  

    


  