from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile

# class UserAdmin(admin.ModelAdmin):
    # This tells the admin which fields to show when EDITING a user
    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     ('Personal info', {'fields': ('email', 'name')}),
    #     ('Permissions', {'fields': ('is_admin', 'is_active')}),
    # )

    # # This tells the admin which fields to show when CREATING a new user
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('username', 'password'),
    #     }),
    # )
    
    # filter_horizontal = ()
    # list_filter = ()
    # list_display = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser')
    # search_fields = ('username',)

admin.site.register(UserProfile)