from django.shortcuts import redirect, render
from .forms import RegistrationForm,ImageUploadForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile, Image


@login_required(login_url='login')
def index(request):
    logged_user = request.user
    images = Image.objects.filter(author__profile__followers__in=[logged_user.id])
    print(images)
    return render(request, 'index.html', {'images':images})

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
def profile(request, id):
    profile = Profile.objects.get(id=id)
    print(id)
    user = profile.user
    images = Image.objects.filter(author=user).all()
    print(images)
    followers = profile.followers.all()
    is_following= None
    for follower in followers:
        if follower == request.user:
            is_following = True
            break
        else:
            is_following = False
    
    count_followers = len(followers)
    
    return render(request, 'profile.html', {'profile': profile, 'images':images, 'user':user,'is_following':is_following,'count_followers':count_followers})

@login_required(login_url='login')
def AddFollower(request, id):
    profile = Profile.objects.get(id=id)
    print(id)
    profile.followers.add(request.user)
    
    return redirect('profile', id=id)

@login_required(login_url='login')
def DeleteFollower(request, id):
    profile = Profile.objects.get(id=id)
    profile.followers.remove(request.user)
    
    return redirect('profile', id=id)
