from django.conf.urls import url

from resources import views as resources_views
from reviews import views as review_views
from . import views

profile = [
    url(r'^$', views.UserProfile.as_view(), name='profile'),
    url(r'^resources/$', views.UserAddedResources.as_view(),
        name='user_resources'),
    url(r'^reviews/$', views.UserAddedReviews.as_view(),
        name='user_reviews'),
    url('resources/(?P<pk>\d+)/edit$', resources_views.UpdateResource.as_view(),
        name='update_resource'),
    url('reviews/(?P<pk>\d+)/edit$', review_views.UpdateReview.as_view(),
        name='update_review'),
]
