from django.shortcuts import redirect, render
from .forms import RegistrationForm,ImageUploadForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile, Image


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def signup(request):
    '''View function that registers a new user'''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email= form.cleaned_data.get('email')
            user.save()
            unhashed_password= form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=unhashed_password)
            login(request, user)
            return redirect('index')
    else:
        form= RegistrationForm()
    title = 'Create Account'
    return render(request, 'signup.html', {'form': form,'title':title})

@login_required(login_url='login')
def upload_image(request):
    current_user = request.user.profile
    
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('index')

    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {"form": form})

@login_required(login_url='login')
def profile(request, user):
    profile = Profile.objects.get(user=user)
    images = Image.objects.filter(profile__user=user).all()
    return render(request, 'profile.html', {'profile': profile, 'images':images})
