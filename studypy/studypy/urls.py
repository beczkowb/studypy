from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from users import views as users_views
from users import urls as users_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^resources/', include('resources.urls')),
    url(r'^tags/', include('tags.urls')),

    url(r'^profile/', include(users_urls.profile)),

    url(r'^login/$', users_views.login, name='login'),
    url(r'^logout/$', users_views.logout, name='logout'),

    # url(r'^profile/reviews$', users_views.UserAddedReviews.as_view(),
    #     name='user_reviews'),
    # url('reviews/(?P<pk>\d+)/edit$', resources_views.UpdateReview.as_view(),
    #     name='update_review'),

    url(r"^select2/", include("django_select2.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
