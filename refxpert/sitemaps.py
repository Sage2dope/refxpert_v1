from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import BlogPost


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return BlogPost.objects.all().order_by('-date_created')

    def lastmod(self, obj):
        return obj.date_created
    


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return ['index', 'about', 'contact', 'tenancy_post', 'legal_post', 'property_post']

    def location(self, item):
        return reverse(item)