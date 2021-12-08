from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image, Comment, Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email',)
    first_name = forms.CharField(label='Your First name', max_length=50)
    last_name = forms.CharField(label='Your Last name', max_length=50)
    
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2', )  
        
class ImageUploadForm(forms.ModelForm):
      class Meta:
          model= Image
          exclude = ['author','likes']
          
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    profile_photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    first_name = forms.CharField(label='Your First name', max_length=50)
    last_name = forms.CharField(label='Your Last name', max_length=50)

    class Meta:
        model = Profile
        fields = ['profile_photo','first_name', 'last_name', 'bio']
        
class UpdateImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    image_caption= forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    image_name = forms.CharField(label='Image name', max_length=50)

    class Meta:
        model= Image
        fields= ['image', 'image_name', 'image_caption']
