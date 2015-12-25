from django.contrib import admin

from . import models


@admin.register(models.Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('url', 'added_by', 'created_at', 'modified_at')
    search_fields = ['description', 'name', 'url']