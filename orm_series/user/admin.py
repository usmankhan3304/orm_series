from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'password','first_name','last_name')
        }),
        ('Personal info', {
            'fields': ()  # Remove 'first_name', 'last_name'
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
    )
    list_display = ('email', 'first_name', 'last_name')  # Keep only valid fields
    ordering=['email']
    search_fields = ("email", "first_name", "last_name")
admin.site.register(CustomUser, CustomUserAdmin)
