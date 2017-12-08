from django.shortcuts import render
from resturant.models import Carousel

def index(request):
	query = Carousel.objects.all()
	context_dict = {'slider': query}
	return render(request,'base.html', context_dict)
	

