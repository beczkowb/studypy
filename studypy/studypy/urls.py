from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

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
    url(r'^reset-password$', auth_views.password_reset,
        {'template_name': 'users/reset_password.html'}, name='password_reset'),
    url(r'^reset-password-complete$', auth_views.password_reset_complete,
        {'template_name': 'users/reset_password_complete.html'},
        name='password_reset_complete'),
    url(r'^reset-password-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$',
        auth_views.password_reset_confirm,
        {'template_name': 'users/reset_password_confirm.html'},
        name='password_reset_confirm'),
    url(r'^reset-password-done$', auth_views.password_reset_done,
        {'template_name': 'users/reset_password_done.html'},
        name='password_reset_done'),


    url(r"^select2/", include("django_select2.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
