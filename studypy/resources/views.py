from django.views.generic import ListView, DetailView, CreateView
from django.conf import settings
from django.core.urlresolvers import reverse_lazy

from .models import Resource, ResourceTag
from .forms import ResourceForm, ResourceFilterForm


class NewestResources(ListView):
    model = Resource
    template_name = 'resources/newest_resources.html'
    context_object_name = 'resources'
    queryset = Resource.get_newest()
    paginate_by = settings.NEWS_PER_PAGE

    def get_queryset(self):
        queryset = super(NewestResources, self).get_queryset()
        if self.request.GET and 'tags' in self.request.GET:
            tags = self.request.GET.getlist('tags')
            tags_set = set(tags)
            filtered_resources = []
            for resource in queryset:
                resource_tags = list([str(r.id) for r in resource.tags.all()])
                resource_tags_set = set(resource_tags)
                if resource_tags_set.intersection(tags_set):
                    filtered_resources.append(resource)
            queryset = filtered_resources
        return queryset

    def get_context_data(self, **kwargs):
        context = super(NewestResources, self).get_context_data(**kwargs)
        if self.request.GET and 'tags' in self.request.GET:
            tags = self.request.GET.getlist('tags')
            context['filter_form'] = ResourceFilterForm(initial={'tags': ResourceTag.objects.filter(id__in=tags)})
        else:
            context['filter_form'] = ResourceFilterForm()

        return context


class Tags(ListView):
    model = ResourceTag
    template_name = 'resources/tags.html'
    context_object_name = 'tags'
    paginate_by = settings.TAGS_PER_PAGE
    queryset = ResourceTag.get_tags_sorted_by_number_of_resources()

    def get_context_data(self, **kwargs):
        context = super(Tags, self).get_context_data(**kwargs)
        tags = context['tags']
        context['tags_grid'] = ResourceTag.get_tags_grid(tags,
                                                         settings.TAGS_PER_ROW)
        return context


class ResourceReviews(DetailView):
    model = Resource
    template_name = 'resources/resource_reviews.html'
    context_object_name = 'resource'


class AddResource(CreateView):
    model = Resource
    template_name = 'resources/add_resource.html'
    form_class = ResourceForm
    success_url = reverse_lazy('newest')

    def get_form_kwargs(self):
        kwargs = super(AddResource, self).get_form_kwargs()
        kwargs['added_by'] = self.request.user
        return kwargs


