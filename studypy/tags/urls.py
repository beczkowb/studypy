from django.conf.urls import url

from . import views

urlpatterns = [
    url('$', views.Tags.as_view(), name='tags'),
]
