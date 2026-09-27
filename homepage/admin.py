from django.contrib import admin

# Register your models here.

from .models import Slide, RepairSlide

class SlideAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'image')

admin.site.register(Slide, SlideAdmin)

class RepairSlideAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'image')

admin.site.register(RepairSlide, RepairSlideAdmin)
