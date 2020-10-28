from django.urls import path
from . import views


urlpatterns = [
  #path('',views.index.as_view(),name='adash'),
  path('home',views.Index,name='dhome'),
  path('dedit/<int:pk>',views.Edit.as_view(),name='dedit'),
  path('<int:ad_id>',views.Detail,name='admin_detail'),
  path('<int:pk>/',views.Admin_Delete,name='admin_delete')
]


#path('delete/<str:pk>/',views.delete,name='delete'),