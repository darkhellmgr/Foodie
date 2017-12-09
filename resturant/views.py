from django.shortcuts import render
from resturant.models import Carousel
from resturant.models import Menu

def index(request):
	query = Carousel.objects.all()
	context_dict = {'slider': query}
	return render(request,'base.html', context_dict)

def menu(request):
	query = Menu.objects.all()
	context_dict = {'menu' : query}
	return render(request, 'base.html', context_dict)
	

