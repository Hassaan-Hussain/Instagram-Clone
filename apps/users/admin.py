from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import UserProfile, UserFollowInfo
from .forms import UserRegistrationForm
from apps.posts.models import UserPosts



class postinline(admin.TabularInline):
    model = UserPosts

class postadmin(UserAdmin):
    # add_form = UserRegistrationForm
    inlines = [
        postinline,
    ]
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username',)
    fieldsets = (
        (None, {'fields': ('bio', 'email', 'profile_image')}),
    )
    add_fieldsets = (
        ('extrafields', {
            'classes': ('wide',),
            'fields': ('username', 'password1','password2', 'bio', 'email', 'profile_image', ),
        }),
    )


admin.site.register(UserProfile, postadmin)

admin.site.register(UserPosts)
admin.site.register(UserFollowInfo)