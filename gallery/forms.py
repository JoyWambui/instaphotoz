from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image

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
          exclude = ['profile']