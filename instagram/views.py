from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages

from apps.users.models import UserProfile
from apps.users.forms import UserRegistrationForm

@login_required(login_url='login')
def home(request):
    user = UserProfile.objects.get(username=request.user)
    context = {
        'user': user,
    }
    return render(request, 'base.html')


