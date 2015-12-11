from django.views.generic import ListView, DetailView
from django.conf import settings

from .models import Resource, ResourceTag


class NewestResources(ListView):
    model = Resource
    template_name = 'resources/newest_resources.html'
    context_object_name = 'resources'
    queryset = Resource.get_newest()
    paginate_by = 3


class Tags(ListView):
    model = ResourceTag
    template_name = 'resources/tags.html'
    context_object_name = 'tags'
    paginate_by = settings.TAGS_PER_PAGE

    def get_context_data(self, **kwargs):
        context = super(Tags, self).get_context_data(**kwargs)
        tags = ResourceTag.get_tags_sorted_by_number_of_resources()
        context['tags_grid'] = ResourceTag.get_tags_grid(tags,
                                                         settings.TAGS_PER_ROW)
        return context


class ResourceReviews(DetailView):
    model = Resource
    template_name = 'resources/resource_reviews.html'
    context_object_name = 'resource'