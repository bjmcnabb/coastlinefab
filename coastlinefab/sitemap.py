from django.contrib.sitemaps import Sitemap

from app.models import Album

class coastlinefabsitemap(Sitemap):
    priority = 0.5
    protocol = 'https'

    def items(self):
        return Album.objects.all()