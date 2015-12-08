from django.views.generic import ListView

from .models import Resource


class Index(ListView):
    model = Resource
    template_name = 'resources/resources.html'
    context_object_name = 'resources'