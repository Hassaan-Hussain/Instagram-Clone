from django.db import models
from apps.users.models import UserProfile


class UserPosts(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to='posts/')
    caption = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.username}' post."


