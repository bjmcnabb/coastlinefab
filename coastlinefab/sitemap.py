from django.contrib.sitemaps import Sitemap

from app.models import Album

class coastlinefabsitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5
    protocol = 'https'

    def items(self):
        return Album.objects.all()