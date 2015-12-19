from django.views.generic import ListView
from django.conf import settings

from .models import Tag


class Tags(ListView):
    model = Tag
    template_name = 'resources/tags.html'
    context_object_name = 'tags'
    paginate_by = settings.TAGS_PER_PAGE
    queryset = Tag.get_tags_sorted_by_number_of_resources()

    def get_context_data(self, **kwargs):
        context = super(Tags, self).get_context_data(**kwargs)
        tags = context['tags']
        context['tags_grid'] = Tag.get_tags_grid(tags, settings.TAGS_PER_ROW)
        return context

