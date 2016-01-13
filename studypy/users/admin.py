from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'password', 'is_superuser', 'first_name', 'last_name', 'email', 'image')
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ['username', 'first_name', 'last_name', 'email']

admin.site.unregister(Group)
