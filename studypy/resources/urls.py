from django.conf.urls import url

from . import views

urlpatterns = [
    url('add/$', views.AddResource.as_view(), name='add_resource'),
    url('newest/$', views.Resources.as_view(resource_list_type='newest'),
        name='newest'),
    url('hot/$', views.Resources.as_view(resource_list_type='hot'), name='hot'),
    url('top-rated/$', views.Resources.as_view(resource_list_type='top_rated'),
        name='top_rated'),
    url('(?P<pk>\d+)/$', views.ResourceDetails.as_view(),
        name='resource_details'),
    url('(?P<pk>\d+)/comments$', views.ResourceComments.as_view(),
        name='resource_comments'),
]
