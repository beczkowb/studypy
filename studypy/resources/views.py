from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponseNotAllowed
from django.contrib.messages.views import SuccessMessageMixin

from braces.views import LoginRequiredMixin

from tags.models import Tag
from comments.forms import ResourceCommentForm
from comments.models import ResourceComment
from .models import Resource
from .forms import ResourceFilterForm, ResourceForm, UpdateResourceForm


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
            context['filter_form'] = ResourceFilterForm(initial={'tags': Tag.objects.filter(id__in=tags)})
        else:
            context['filter_form'] = ResourceFilterForm()

        return context


class HotResources(ListView):
    model = Resource
    template_name = 'resources/hot_resources.html'
    context_object_name = 'resources'
    queryset = Resource.get_hot()
    paginate_by = settings.NEWS_PER_PAGE

    def get_queryset(self):
        queryset = super(HotResources, self).get_queryset()
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
        context = super(HotResources, self).get_context_data(**kwargs)
        if self.request.GET and 'tags' in self.request.GET:
            tags = self.request.GET.getlist('tags')
            context['filter_form'] = ResourceFilterForm(initial={'tags': Tag.objects.filter(id__in=tags)})
        else:
            context['filter_form'] = ResourceFilterForm()

        return context


class AddResource(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Resource
    template_name = 'resources/add_resource.html'
    form_class = ResourceForm
    success_url = reverse_lazy('newest')
    success_message = "Resource added successfully"

    def get_form_kwargs(self):
        kwargs = super(AddResource, self).get_form_kwargs()
        kwargs['added_by'] = self.request.user
        return kwargs


class ResourceDetails(DetailView):
    model = Resource
    template_name = 'resources/resource_details.html'
    context_object_name = 'resource'


class ResourceComments(SuccessMessageMixin, CreateView):
    model = ResourceComment
    template_name = 'resources/resource_comments.html'
    form_class = ResourceCommentForm
    success_message = 'Comment added successfully'

    def get_initial(self):
        initial = super(ResourceComments, self).get_initial()
        if self.request.method == 'GET':
            resource = Resource.objects.get(pk=self.kwargs['pk'])
            author = self.request.user
            initial = {'resource': resource, 'author': author}
        return initial

    def get_form_kwargs(self):
        kwargs = super(ResourceComments, self).get_form_kwargs()
        if self.request.method == 'POST':
            resource = Resource.objects.get(pk=self.kwargs['pk'])
            author = self.request.user
            kwargs.update({'resource': resource, 'author': author})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(ResourceComments, self).get_context_data(**kwargs)
        context['resource'] = Resource.objects.get(pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('resource_comments', kwargs={'pk': self.kwargs['pk']})

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated():
            return HttpResponseNotAllowed
        return super(ResourceComments, self).post(request, *args, **kwargs)


class UpdateResource(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Resource
    form_class = UpdateResourceForm
    template_name = 'resources/update_resource.html'
    context_object_name = 'form'
    success_url = reverse_lazy('user_resources')
    success_message = 'Resource updated successfully'

    def get(self, request, *args, **kwargs):
        resource_pk = kwargs['pk']
        resource = Resource.objects.get(pk=resource_pk)
        resource_was_added_by_user = resource.added_by == request.user
        if not resource_was_added_by_user:
            raise Http404
        return super(UpdateResource, self).get(request, *args, **kwargs)