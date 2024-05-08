from django.contrib import admin
from core.models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from django.contrib import admin
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'date_opened', 'latitude', 'longtitude']
