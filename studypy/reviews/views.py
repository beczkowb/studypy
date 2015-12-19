from django.views.generic import DetailView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.http import Http404

from .forms import UpdateReviewForm, ReviewForm
from resources.models import Resource, Review


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
