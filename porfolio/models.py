from django.db import models

# Create your models here.


class Project(models.Model):
	title = models.CharField(max_length=200)
	descrciption = models.TextField()
	image = models.ImageField()
	#registra la fecha de creacion
	created =models.DateTimeField(auto_now_add=True)
	#registra la fecha de modificacion
	update = models.DateTimeField(auto_now=True)
