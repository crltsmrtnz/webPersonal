from django.shortcuts import render

# Create your views here.


def home (request):
	return render (request, "core/home.html")

def about (request):
	return render (request, "core/about.html")

def porfolio (request):
	return render (request, "core/porfolio.html")

def contact (request):
	return render (request, "core/contact.html")