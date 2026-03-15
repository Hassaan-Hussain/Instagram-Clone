from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PostForm
from apps.users.models import UserProfile
from .models import UserPosts

def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.info(request, 'Post Successfully Created!')
        return redirect('home')
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/upload_posts.html', context)

def edit_post(request, pk):
    post = UserPosts.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
    }
    return render(request, 'posts/edit_post.html', context)

def delete_post(request, pk):
    post = UserPosts.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('profile', username=request.user.username)
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
    }
    return render(request, 'posts/delete_post.html', context)