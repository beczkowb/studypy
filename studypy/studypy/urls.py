from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy

from users import views as users_views
from users import urls as users_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^resources/', include('resources.urls')),
    url(r'^reviews/', include('reviews.urls')),
    url(r'^tags/', include('tags.urls')),

    url(r'^profile/', include(users_urls.profile)),

    url(r'^login/$', users_views.login, name='login'),
    url(r'^logout/$', users_views.logout, name='logout'),
    url(r'^register/$', users_views.Register.as_view(), name='register'),


    url(r"^select2/", include("django_select2.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
