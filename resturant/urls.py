from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns =[ 
	url(r'^$', views.index , name= "index"),
	url(r'^menu/$', views.menu , name= "menu"),
	url(r'^check/$',views.check,name='check')

]