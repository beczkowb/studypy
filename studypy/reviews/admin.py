from django.contrib import admin

from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('resource', 'author', 'created_at', 'modified_at')
    search_fields = ('contents', )