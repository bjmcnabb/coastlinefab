from django.contrib import admin

# Register your models here.

from .models import Slide

class SlideAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'image')

admin.site.register(Slide, SlideAdmin)