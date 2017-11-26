from django.shortcuts import render
from .models import Dog
# Create your views here.

def HomeView(request) :

	dogs = Dog.objects.all()

	for dog in dogs :
		print(dog.name)

	return render(request, './index_html.html')

def AboutView(request) :

	return render(request, './about_us.html')


