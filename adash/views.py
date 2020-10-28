from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from ad.models import *
from django.contrib.auth.models import User
from django.urls import reverse_lazy


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
   return render(request,'admin_dash/index.html',context)
  else:
    return redirect('home')





def Detail(request,ad_id):
  user = User
  if user.is_staff == True:
     ad = get_object_or_404(Ad,pk=ad_id)
     context = {'ad':ad,}
     return render(request,'admin_dash/admin_detail.html',context)
  else:
    return redirect('home')



""" def ad(request,ad_id):
  ad = get_object_or_404(Ads,pk=ad_id)
  context = {'ad':ad,}
  return render(request,'ads/ad.html',context) """





class Edit(UpdateView):
  model  = Ad 
  fields = '__all__'
  template_name = 'admin_dash/edit.html'
  success_url = reverse_lazy('dhome')

 


""" def Home(request):
  if User.is_supruser:
    ads = Ad.objects.all()
    context = {'ads':ads}
  else:
     return redirect('login')
  return render(request,'adash/index.html',context)
 """
  

