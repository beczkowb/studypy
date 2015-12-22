from django.views.generic import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponseNotAllowed
from django.contrib.messages.views import SuccessMessageMixin

from braces.views import LoginRequiredMixin

from resources.models import Resource, Review
from comments.models import ReviewComment
from comments.forms import ReviewCommentForm
from .forms import UpdateReviewForm, ReviewForm


class UpdateReview(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
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


class AddReview(LoginRequiredMixin, SuccessMessageMixin, CreateView):
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


class ReviewComments(SuccessMessageMixin, CreateView):
    model = ReviewComment
    template_name = 'reviews/review_comments.html'
    form_class = ReviewCommentForm
    success_message = 'Comment added successfully'

    def get_initial(self):
        initial = super(ReviewComments, self).get_initial()
        if self.request.method == 'GET':
            review = Review.objects.get(pk=self.kwargs['pk'])
            author = self.request.user
            initial = {'review': review, 'author': author}
        return initial

    def get_form_kwargs(self):
        kwargs = super(ReviewComments, self).get_form_kwargs()
        if self.request.method == 'POST':
            review = Review.objects.get(pk=self.kwargs['pk'])
            author = self.request.user
            kwargs.update({'review': review, 'author': author})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(ReviewComments, self).get_context_data(**kwargs)
        context['review'] = Review.objects.get(pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('review_comments', kwargs={'pk': self.kwargs['pk']})

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated():
            return HttpResponseNotAllowed
        return super(ReviewComments, self).post(request, *args, **kwargs)

