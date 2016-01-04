from django.conf import settings
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponseBadRequest

from .models import Tag
from .forms import TagForm


class Tags(View):
    def get(self, request, *args, **kwargs):
        context = {}
        tags = Tag.get_tags_sorted_by_number_of_resources()
        context['tags_grid'] = Tag.get_tags_grid(tags, settings.TAGS_PER_ROW)
        tag_form = TagForm()
        context['form'] = tag_form
        return render(request, 'tags/tags.html', context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseBadRequest()
        context = {}
        tag_form = TagForm(request.POST)
        if tag_form.is_valid():
            tag_form.save()
            tag_form = TagForm()
        context['form'] = tag_form
        tags = Tag.get_tags_sorted_by_number_of_resources()
        context['tags_grid'] = Tag.get_tags_grid(tags, settings.TAGS_PER_ROW)
        return render(request, 'tags/tags.html', context)