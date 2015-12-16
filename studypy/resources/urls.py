from django.conf.urls import url

from . import views

urlpatterns = [
    url('add/$', views.AddResource.as_view(), name='add_resource'),
    url('newest/$', views.NewestResources.as_view(), name='newest'),
    url('hot/$', views.HotResources.as_view(), name='hot'),
    url('tags/$', views.Tags.as_view(), name='tags'),
    url('(?P<pk>\d+)/reviews/$', views.ResourceReviews.as_view(),
        name='resource_reviews'),
    url('(?P<pk>\d+)/reviews/add$', views.AddReview.as_view(),
        name='add_review'),
    url('(?P<pk>\d+)/edit$', views.UpdateResource.as_view(),
        name='update_resource'),
]
