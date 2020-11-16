from django.urls import path
from . import views

app_name='property'

urlpatterns = [
    path('', views.RoomList.as_view(),name='RoomList'),
    path('<int:pk>', views.RoomDetail.as_view(),name='RoomDetail'),
  

]