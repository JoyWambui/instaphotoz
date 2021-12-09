from django.shortcuts import redirect, render
from .forms import RegistrationForm,ImageUploadForm,CommentForm,UpdateUserForm,UpdateProfileForm,UpdateImageForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Comment, Profile, Image
from django.contrib.auth.models import User



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
    if request.user.is_authenticated:
        return redirect('index')
    
    return render(request, 'signup.html', {'form': form,'title':title})

@login_required(login_url='login')
def upload_image(request):
    current_user = request.user
    
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = current_user
            image.save()
        return redirect('profile', id=current_user.id)

    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {"form": form})

@login_required(login_url='login')
def update_image(request, id):
    got_image = Image.objects.get(id=id)
    current_user = request.user.profile

    if request.method == 'POST':
        form = UpdateImageForm(request.POST, request.FILES, instance=got_image)
        if form.is_valid():
            form.save()
        return redirect('profile', id=current_user.id)

    else:
        form = ImageUploadForm(instance=got_image)
    return render(request, 'update_image.html', {"form": form})

@login_required(login_url='login')
def delete_image(request, id):
    Image.objects.filter(id=id).delete() 
    return redirect('profile', id=request.user.id)



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
def update_profile(request, id):
    profile = Profile.objects.get(id=id)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile' ,id=id)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'update_profile.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required(login_url='login')
def delete_profile(request):
    Profile.objects.filter(id=request.user.id).delete()
    User.objects.filter(id=request.user.id) .delete()
    return redirect('login')


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

@login_required(login_url='login')
def image(request, id):
    image = Image.objects.get(id=id)
    user = image.author
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_author = request.user
            comment.comment_image = image
            comment.save()
        return redirect('imageDetail', id=id)

    else:
        form = CommentForm()
        
    likes = image.likes.all()
    liked = None
    for like in likes:
        if like == request.user:
            liked = True
            break
        else:
            liked = False
    
    count_likes = len(likes)

    comments= Comment.objects.filter(comment_image=image).order_by('-created')
    
    return render(request, 'image_details.html', {'form': form, 'image': image, 'comments': comments,'liked':liked,'count_likes':count_likes,'user':user})

@login_required(login_url='login')
def like(request,id):
    image = Image.objects.get(id=id)
    image.likes.add(request.user)

    return redirect('imageDetail', id=id)

@login_required(login_url='login')
def unlike(request,id):
    image = Image.objects.get(id=id)
    image.likes.remove(request.user)

    return redirect('imageDetail', id=id)