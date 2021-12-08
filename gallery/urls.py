
from django.urls import path

from . import views


urlpatterns= [
    path('',views.index, name='index'),
    path('new_upload/',views.upload_image, name='uploadImage'),
    path('profile/<int:id>/',views.profile, name='profile'),
    path('profile/<int:id>/followers/add', views.AddFollower, name='addFollower'),
    path('profile/<int:id>/followers/delete', views.DeleteFollower, name='deleteFollower'),
]