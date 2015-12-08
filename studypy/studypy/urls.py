from django.conf.urls import include, url
from django.contrib import admin

from resources.views import Index


urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^resources/', include('resources.urls')),

]
