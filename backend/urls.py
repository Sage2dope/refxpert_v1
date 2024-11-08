
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from refxpert.sitemaps import PostSitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.static import serve
from django.urls import re_path


sitemaps = {
    'post': PostSitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path("kareem/", admin.site.urls),
    path('sitemap.xml', sitemap,{'sitemaps': sitemaps}),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", include("refxpert.urls")),
]

# Change when website starts getting more traffic and site becomes slow 
if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]