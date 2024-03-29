from django.contrib import admin

from . import models


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name',]