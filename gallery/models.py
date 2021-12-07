from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Profile(models.Model):
    '''Model that defines a user profile and its methods'''
    user = models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='images/', blank=True)
    bio = tinymce_models.HTMLField()
    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    email = models.EmailField()
    
    @receiver(post_save, sender=User)
    def save_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
        
    # def get_user_profile()
    
class Image(models.Model):
    '''Model that defines an image upload and its methods'''
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.image_name

        