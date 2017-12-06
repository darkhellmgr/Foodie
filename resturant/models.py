from django.db import models

class Carousel(models.Model):
	slider_image = models.ImageField(null = True, blank = True, upload_to = 'slider/%Y/%m/%d',)
	display_title = models.CharField(max_length = 100,)
	url = models.URLField(null=True, blank=True,)
	display_content = models.TextField(null=True,blank=True,)

	
