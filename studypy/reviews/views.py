from django.views.generic import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.contrib.messages.views import SuccessMessageMixin


from .forms import UpdateReviewForm, ReviewForm
from resources.models import Resource, Review


class UpdateReview(SuccessMessageMixin, UpdateView):
    model = Review
    form_class = UpdateReviewForm
    template_name = 'reviews/update_review.html'
    context_object_name = 'form'
    success_url = reverse_lazy('user_reviews')
    success_message = 'Review updated successfully'

    def get(self, request, *args, **kwargs):
        review_pk = kwargs['pk']
        review = Review.objects.get(pk=review_pk)
        review_was_added_by_user = review.author == request.user
        if not review_was_added_by_user:
            raise Http404
        return super(UpdateReview, self).get(request, *args, **kwargs)


class AddReview(SuccessMessageMixin, CreateView):
    model = Review
    template_name = 'reviews/add_review.html'
    form_class = ReviewForm
    success_message = 'Review added successfully'

    def get_form_kwargs(self):
        kwargs = super(AddReview, self).get_form_kwargs()
        kwargs['author'] = self.request.user
        kwargs['resource'] = Resource.objects.get(pk=self.kwargs['pk'])
        return kwargs

    def get_success_url(self):
        return reverse_lazy('resource_details',
                            kwargs={'pk': self.kwargs['pk']})
