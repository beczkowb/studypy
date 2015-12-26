from django.conf.urls import url

from . import views

urlpatterns = [
    url('add/$', views.AddResource.as_view(), name='add_resource'),
    url('newest/$', views.NewestResources.as_view(), name='newest'),
    url('hot/$', views.HotResources.as_view(), name='hot'),
    url('(?P<slug>[-\w\d]+)/$', views.ResourceDetails.as_view(),
        name='resource_details'),
    url('(?P<pk>\d+)/comments$', views.ResourceComments.as_view(),
        name='resource_comments'),
]
