from django.views.generic import ListView

from .models import Resource


class NewestResources(ListView):
    model = Resource
    template_name = 'resources/newest_resources.html'
    context_object_name = 'resources'
    queryset = Resource.get_newest()
    paginate_by = 2