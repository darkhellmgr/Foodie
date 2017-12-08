from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns =[ 
	url(r'^$', views.index , name= "base"),
	url(r'^contact/$', login, {'template_name':'sources/login.html'})

]