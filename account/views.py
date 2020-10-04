from django.shortcuts import render,redirect 
from django.contrib import messages,auth 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 

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




def Dashboard(request):
  return render(request,'account/dashboard.html')