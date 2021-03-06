
from django.urls import path

from . import views


urlpatterns= [
    path('',views.index, name='index'),
    path('new_upload/',views.upload_image, name='uploadImage'),
    path('profile/<int:id>/',views.profile, name='profile'),
    path('profile/<int:id>/update/', views.update_profile,name='updateProfile'),
    path('profile/delete/', views.delete_profile, name='deleteProfile'),
    path('profile/<int:id>/followers/add/', views.AddFollower, name='addFollower'),
    path('profile/<int:id>/followers/delete/', views.DeleteFollower, name='deleteFollower'),
    path('image/<int:id>/',views.image, name='imageDetail'),
    path('image/<int:id>/like/', views.like, name='like'),
    path('image/<int:id>/unlike/', views.unlike, name='unlike'),
    path('image/<int:id>/update/', views.update_image, name='updateImage'),
    path('image/<int:id>/delete/', views.delete_image, name='deleteImage'),
    path('profiles/', views.profiles, name='profiles')



]