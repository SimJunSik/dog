from django.shortcuts import render
from .models import Dog, User
from django.http import JsonResponse
from django.core.urlresolvers import reverse
# Create your views here.

def HomeView(request) :

	if(request.path == '/') :

		user = User.objects.get(id_str="unknown")

		context = {'user' : user}


	else :

		id_str = request.POST['id']

		user = User.objects.get(id_str=id_str)

		context = {'user' : user}

		print(id_str)

	return render(request, './index_html.html', context)



def AboutView(request) :

	return render(request, './about_us.html')


def StatsView(request) :

	return render(request, './stats.html')


def ShelterView(request) :

	return render(request, './site.html')


def MembershipView(request) :

	return render(request, './membership.html')

def MatchingView(request) :

	return render(request, './matching.html')


def LoginView(request) :

	return render(request, './login.html')


def tmp(request) :

	id_str = request.POST['id']
	psw_str = request.POST['psw']

	user = User(id_str = id_str, psw_str = psw_str, auth = 1)
	user.save()

	context = {'user' : user}
	return render(request, './login.html', context)


def validate_username(request):

    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(id_str=username).exists()
    }

    if data['is_taken']:
        data['error_message'] = '이미 존재하는 ID입니다.'
    return JsonResponse(data)