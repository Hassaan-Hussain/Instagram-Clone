from django import forms
from .models import UserPosts


class PostForm(forms.ModelForm):
    class Meta:
        model = UserPosts
        fields = ('post_image', 'caption')