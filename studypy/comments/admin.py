from django.contrib import admin

from .models import ResourceComment, ReviewComment


admin.site.register(ResourceComment)
admin.site.register(ReviewComment)
