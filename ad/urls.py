from django.urls import path
from . import views

urlpatterns = [
  path('',views.Home.as_view(),name='ads'),
  path('create/',views.CreateAd.as_view(),name='create')
]
