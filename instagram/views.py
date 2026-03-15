from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages

from apps.users.models import UserProfile
from apps.posts.models import UserPosts

@login_required(login_url='login')
def home(request):
    user = UserProfile.objects.get(username=request.user)
    posts = UserPosts.objects.filter(author=request.user)
    context = {
        'user': user,
        'posts': posts,
    }
    return render(request, 'base.html', context)


