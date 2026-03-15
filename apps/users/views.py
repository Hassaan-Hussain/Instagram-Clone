from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from .forms import UserRegistrationForm
from .models import UserProfile
from apps.posts.models import UserPosts

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            print('error message')
            messages.info(request, 'Invalid Credentials!')

    return render(request, 'registration/login.html')
    
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/register.html', context)

def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out!")
    return redirect('login')

def profile(request, username):
    user = UserProfile.objects.get(username=username)
    posts = UserPosts.objects.filter(author=request.user)
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'users/profile.html', context)

def edit_profile(request, username):
    user = UserProfile.objects.get(username=username)
    if request.method == 'POST':
        profile_image = request.FILES.get('profile_image')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        birth_date = request.POST.get('dob')
        
        user.profile_image = profile_image if profile_image else user.profile_image
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.bio = bio
        user.birth_date = birth_date if birth_date else user.birth_date
        user.save()
        return redirect('profile', username=user.username)

    context = {
        'user': user,
    }
    return render(request, 'users/edit_profile.html', context)