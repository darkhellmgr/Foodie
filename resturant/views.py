from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect,HttpResponseNotFound
from resturant.models import Carousel
from resturant.models import Menu

def index(request):
	query = Carousel.objects.all()
	context_dict = {'slider': query}
	return render(request,'base.html', context_dict)

def menu(request):
	query = Menu.objects.all()
	context_dict = {'menu' : query}
	return render(request, 'sources/menu.html', context_dict)
	

