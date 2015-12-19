from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.http import Http404

from .models import Resource, ResourceTag, Review
from .forms import ResourceForm, ResourceFilterForm, ReviewForm, UpdateResourceForm, UpdateReviewForm


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


class AddReview(CreateView):
    model = Review
    template_name = 'resources/add_review.html'
    form_class = ReviewForm

    def get_form_kwargs(self):
        kwargs = super(AddReview, self).get_form_kwargs()
        kwargs['author'] = self.request.user
        kwargs['resource'] = Resource.objects.get(pk=self.kwargs['pk'])
        return kwargs

    def get_success_url(self):
        return reverse_lazy('resource_reviews',
                            kwargs={'pk': self.kwargs['pk']})


class UpdateResource(UpdateView):
    model = Resource
    form_class = UpdateResourceForm
    template_name = 'resources/update_resource.html'
    context_object_name = 'form'
    success_url = reverse_lazy('user_resources')

    def get(self, request, *args, **kwargs):
        resource_pk = kwargs['pk']
        resource = Resource.objects.get(pk=resource_pk)
        resource_was_added_by_user = resource.added_by == request.user
        if not resource_was_added_by_user:
            raise Http404
        return super(UpdateResource, self).get(request, *args, **kwargs)


class UpdateReview(UpdateView):
    model = Review
    form_class = UpdateReviewForm
    template_name = 'resources/update_review.html'
    context_object_name = 'form'
    success_url = reverse_lazy('user_reviews')

    def get(self, request, *args, **kwargs):
        review_pk = kwargs['pk']
        review = Review.objects.get(pk=review_pk)
        review_was_added_by_user = review.author == request.user
        if not review_was_added_by_user:
            raise Http404
        return super(UpdateReview, self).get(request, *args, **kwargs)