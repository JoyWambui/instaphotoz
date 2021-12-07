
from django.urls import path

from . import views


urlpatterns= [
    path('',views.index, name='index'),
    path('new_upload/',views.upload_image, name='uploadImage'),
    path('profile/<user>',views.profile, name='profile'),


]