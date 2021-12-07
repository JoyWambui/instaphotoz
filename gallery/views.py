from django.shortcuts import redirect, render
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile


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

    