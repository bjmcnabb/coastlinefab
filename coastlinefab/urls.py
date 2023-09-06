"""coastlinefab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# ---NEW---
from django.contrib.auth import views
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

import app.forms
import app.views

from django.conf.urls import include
# ------

from django.contrib import admin
admin.autodiscover()

from django.urls import include, path, re_path

# from django.contrib.sitemaps.views import sitemap
# from coastlinefab.sitemap import coastlinefabsitemap

# sitemaps = {"sitemaps": coastlinefabsitemap()}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("homepage.urls")),
    path('contact/', include("contact.urls")),
    path('gallery/', include("app.urls")),
    # path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap",),
    # path('<slug:slug>', gallery.views.AlbumDetail.as_view(), name='album'),
    

    # ---NEW---
    # re_path(r'^$', app.views.gallery, name='gallery'),
    # re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/icons/favicon.ico', permanent=True)),
    # re_path(r'^(?P<slug>[-\w]+)$', app.views.AlbumDetail.as_view(), name='album'), #app.views.AlbumView.as_view()
    
    # Auth related urls
    
    re_path(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    re_path(r'^logout$', views.LogoutView.as_view(), { 'next_page': '/', }, name='logout'),
    re_path(r'^robots\.txt', include('robots.urls')),
    

    # ------
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'app.views.handler404'