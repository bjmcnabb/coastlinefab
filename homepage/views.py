from django.shortcuts import render

# Create your views here.
from homepage.models import Slide

def home(request):
	slides = Slide.objects.all()
	return render(request, 'homepage.html', {"slides":slides})
