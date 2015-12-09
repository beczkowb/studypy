from django.conf.urls import include, url

from . import views


urlpatterns = [
    url('newest/$', views.NewestResources.as_view(), name='newest')
]
