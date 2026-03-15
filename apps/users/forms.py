from  django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('email','first_name', 'last_name', 'username', 'profile_image', 'bio', 'birth_date')