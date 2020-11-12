from django.shortcuts import render,redirect
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from . models import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class Home(ListView):
 # model = Ad
  queryset = Ad.objects.filter(status='publish')
  template_name = 'ads/ads.html'
  context_object_name = 'ads'



@method_decorator(login_required, name='dispatch')
class CreateAd(CreateView):
  model = Ad 
  fields = ('title','location','region','category','condition','price','brand','negotiable','main_photo','photo_1','photo_2','photo_3','description')
  template_name = 'ads/create.html'
  success_url = reverse_lazy('ads')

  def form_valid(self, form):
    form.instance.seller = self.request.user
    form.save()
    return super(CreateAd, self).form_valid(form)
    





class AdDetail(DetailView):
    model = Ad
    template_name='ads/detial.html'




def Search(request):

  ads = Ad.objects.all()
  if 'keyword' in request.GET:
    keyword = request.GET['keyword']
    if keyword:
      ads = ads.filter(description__icontains=keyword,)

  context = {'ads':ads,}

  return render(request,'ads/ad_search.html',context)