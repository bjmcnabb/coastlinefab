from django.shortcuts import render

# Create your views here.
from homepage.models import Slide, RepairSlide

def home(request):
	slides = Slide.objects.all()
	repairslides = RepairSlide.objects.all()
	return render(request, 'homepage.html', {"slides":slides, "repairslides":repairslides})
