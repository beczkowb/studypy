from django.conf.urls import include, url
from django.contrib import admin

from users import views as users_views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^resources/', include('resources.urls')),
    url(r'^login/$', users_views.login, name='login'),
    url(r'^logout/$', users_views.logout, name='logout'),
]
