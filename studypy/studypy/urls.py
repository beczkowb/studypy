from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from users import views as users_views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^resources/', include('resources.urls')),
    url(r'^login/$', users_views.login, name='login'),
    url(r'^logout/$', users_views.logout, name='logout'),
    url(r'^profile/$', users_views.UserProfile.as_view(), name='profile'),

    url(r"^select2/", include("django_select2.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
