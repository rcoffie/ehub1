from django.shortcuts import render

# Create your views here.


def Login(request):
  return render(request,'account/login.html')




def Register(request):
  return render(request,'account/registration.html')