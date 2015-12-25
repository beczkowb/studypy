from django.contrib import admin

from .models import ResourceComment, ReviewComment


@admin.register(ResourceComment)
class ResourceCommentAdmin(admin.ModelAdmin):
    list_display = ('resource', 'author', 'contents')
    search_fields = ['resource__name', 'resource__description',
                     'author__username', 'author__first_name',
                     'author__last_name', 'contents']


@admin.register(ReviewComment)
class ReviewCommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'author', 'contents')
    search_fields = ['review__contents', 'author__username',
                     'author__first_name', 'author__last_name',
                     'contents']

