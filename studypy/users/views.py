from django.shortcuts import render, redirect
from django.contrib.auth import logout as logout_user
from django.views.decorators.http import require_http_methods
from django.views.generic import UpdateView, ListView
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin

from resources.models import Resource, Review
from .forms import LoginForm, UserProfileForm


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('newest')
        else:
            return render(request, 'users/login.html', {'form': form})


@require_http_methods(["GET"])
def logout(request):
    if request.user.is_authenticated():
        logout_user(request)
        return redirect('newest')
    return redirect('login')


class UserProfile(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserAddedResources(LoginRequiredMixin, ListView):
    model = Resource
    template_name = 'users/user_added_resources.html'
    context_object_name = 'resources'

    def get_queryset(self):
        return Resource.objects.filter(added_by=self.request.user)


class UserAddedReviews(LoginRequiredMixin, ListView):
    model = Resource
    template_name = 'users/user_added_reviews.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        return Review.objects.filter(author=self.request.user)

