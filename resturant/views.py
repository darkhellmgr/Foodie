from django.shortcuts import render
from resturant.models import Carousel

def index(request):
	return render(request, 'base.html')

def home(request):
	query = Carousel.object.all()
	context_dict = {'slider': query}
	return render(request,'base.html', context_dict)
