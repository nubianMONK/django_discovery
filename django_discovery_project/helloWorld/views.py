from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	context_dict = {'boldmessage': "I am bold font from the context"}


	return render(request,'helloWorld/index.html', context_dict)


def about(request):
	return HttpResponse("Akin says this is the about page <br/><a href='/helloWorld/'>Index</a>")
