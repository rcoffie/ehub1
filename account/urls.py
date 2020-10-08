from django.urls import path
from . import views

urlpatterns = [
  path('register/',views.Register,name='register'),
  path('login/',views.Login,name='login'),
  path('dashboard/',views.Dashboard.as_view(),name='dashboard'),
  path('d_detail/<int:pk>',views.Dashboard_Detail.as_view(),name='d_detail')
]
