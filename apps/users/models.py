from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    profile_image = models.ImageField(blank=True, upload_to='media')
    bio = models.TextField(max_length=250, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.username}"
    

class UserFollowInfo(models.Model):
    follower = models.CharField()
    following = models.CharField()
    
    def  __str__(self):
        return f"{self.follower} following {self.following}"