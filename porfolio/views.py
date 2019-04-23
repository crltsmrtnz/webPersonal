from django.shortcuts import render
from .models import project
# Create your views here.

def porfolio (request):
	projects = project.objects.all()
	
	return render (request, "porfolio/porfolio.html", {'projects':projects})
	
