from django.conf.urls import url

from . import views

urlpatterns = [
    url('(?P<pk>\d+)/add$', views.AddReview.as_view(),
        name='add_review'),
    url('(?P<pk>\d+)/comments$', views.ReviewComments.as_view(),
        name='review_comments'),
]
