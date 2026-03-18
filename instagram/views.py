from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages

from apps.users.models import UserProfile, UserFollowInfo
from apps.posts.models import UserPosts

from itertools import chain

@login_required(login_url='login')
def home(request):
    user = UserProfile.objects.get(username=request.user)
    posts = UserPosts.objects.filter(author=request.user)
    all_users = UserProfile.objects.all()
    following = UserFollowInfo.objects.filter(follower=request.user.username).values_list('following', flat=True)
    context = {
        'user': user,
        'posts': posts,
        'all_users': all_users,
        'following_list': list(following),
    }
    return render(request, 'base.html', context)

@require_POST
def follow(request, username):
    follow_obj = UserFollowInfo.objects.get_or_create(follower=request.user.username, following=username)
    return redirect('home')

@require_POST
def unfollow(request, username):
    follow_obj = UserFollowInfo.objects.get(follower=request.user.username, following=username).delete()
    return redirect('home')

