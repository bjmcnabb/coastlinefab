from django.urls import path, re_path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
	path('', views.gallery, name='gallery'),
    # re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/icons/favicon.ico', permanent=True)),
    # re_path(r'^(?P<slug>[-\w]+)$', views.AlbumDetail.as_view(), name='album'), #gallery.views.AlbumView.as_view()  
    path('<slug:slug>', views.AlbumDetail.as_view(), name='album')
]