from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.urls import reverse
from django.core import serializers
import json
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.

def HomeView2(request) :

	import sys, os
	from django.conf import settings
	import codecs
	from bs4 import BeautifulSoup
	import urllib.request
	from urllib.parse import quote
	from urllib.request import Request, urlopen
	from django.shortcuts import render_to_response
	import urllib

	f = open('dogapp/보호소리스트.txt', 'r+')
	cnt = 0
	name = []
	addr = []
	num = []
	location = []
	location_list = ['서울', '인천', '경기도', '강원도', '충청북도', '대전', '충청남도', '경상북도', '전라북도', '광주', '전라남도', '경상남도', '부산', '울산', '세종', '대구' ,'제주']

	while True:
	    line = f.readline()
	    if not line: break

	    tmp = ''

	    #print(line)
	    for ch in line :
	   		#print(ch)
	   		if ch=='\t' or ch=='\n':
	   			cnt = cnt+1
	   			if(cnt%3 == 1) :
	   				name.append(tmp)
	   			if(cnt%3 == 2) :
	   				addr.append(tmp)
	   				for item in location_list :
	   					if item in tmp[0:5] :
	   						location.append(item)


	   			if(cnt%3 == 0) :
	   				num.append(tmp)
	   			tmp = ''

	   		else :
	   			tmp += ch


	for i in range(0, len(name)) :
		shelter = Shelter(name = name[i], addr = addr[i], num = num[i], location = location[i])
		shelter.save()


	shelters = Shelter.objects.all()

	context = {'shelters' : shelters}

	return render(request, "./home.html", context)

def HomeView(request) :

	"""
	if(request.path == '/') :

		user = User.objects.get(id_str="unknown")

		#context = {'user' : user}


	else :

		id_str = request.POST['id']

		user = User.objects.get(id_str=id_str)

		#context = {'user' : user}

		print(id_str)
	"""

	return render(request, './index_html.html')

def ShelterView(request) :

	shelters = Shelter.objects.all()

	context = {'shelters' : shelters}

	return render(request, './shelter.html', context)

def GetAddr(request) :

	num = request.GET.get('num', None)

	shelter = Shelter.objects.get(num = num)

	addr = shelter.addr

	data = {'addr' : addr}

	return JsonResponse(data)



def NoticeView(request) :

	json_serializer = serializers.get_serializer("json")()
	markers = json_serializer.serialize(Marker.objects.all(), ensure_ascii=False)

	dogs = Marker.objects.all()

	context = {'markers' : markers, 'dogs' : dogs}

	if request.method == 'POST' and request.FILES['dog_image'] :
		img_src = request.FILES['dog_image']
		fs = FileSystemStorage()
		filename = fs.save(img_src.name, img_src)
		uploaded_file_url = fs.url(filename)
		#print(uploaded_file_url)

		location_name = request.POST.get('location_name')
		print(location_name)
		lat = request.POST.get('lat')
		lng = request.POST.get('lng')
		print(lat, lng)
		dog_name = request.POST.get('dog_name')
		psw_txt = request.POST.get('psw_txt')
		#print(location_name, lat, lng)

		pk_value = request.POST.get('pk_value')
		#print(pk_value)
		if pk_value == 'none'  or len(pk_value)==0 :
			marker = Marker(location_name = location_name, x = lat, y = lng, dog_name = dog_name, img_src = uploaded_file_url, psw = psw_txt)
			marker.save()
		else :
			marker = Marker.objects.get(pk=pk_value)
			marker.location_name = location_name
			marker.x = lat
			marker.y = lng
			marker.dog_name = dog_name
			marker.psw = psw_txt
			marker.img_src = uploaded_file_url
			marker.save()

	return render(request, './notice_test.html', context)



def TakedogView(request) :

	json_serializer = serializers.get_serializer("json")()
	markers = json_serializer.serialize(TakeMarker.objects.all(), ensure_ascii=False)

	dogs = TakeMarker.objects.all()

	context = {'markers' : markers, 'dogs' : dogs}

	if request.method == 'POST' and request.FILES['dog_image'] :
		img_src = request.FILES['dog_image']
		fs = FileSystemStorage()
		filename = fs.save(img_src.name, img_src)
		uploaded_file_url = fs.url(filename)
		#print(uploaded_file_url)

		location_name = request.POST.get('location_name')
		print(location_name)
		lat = request.POST.get('lat')
		lng = request.POST.get('lng')
		print(lat, lng)
		dog_name = request.POST.get('dog_name')
		psw_txt = request.POST.get('psw_txt')
		#print(location_name, lat, lng)

		pk_value = request.POST.get('pk_value')
		#print(pk_value)
		if pk_value == 'none' or len(pk_value)==0 :
			marker = TakeMarker(location_name = location_name, x = lat, y = lng, dog_name = dog_name, img_src = uploaded_file_url, psw = psw_txt)
			marker.save()
		else :
			marker = TakeMarker.objects.get(pk=pk_value)
			marker.location_name = location_name
			marker.x = lat
			marker.y = lng
			marker.dog_name = dog_name
			marker.psw = psw_txt
			marker.img_src = uploaded_file_url
			marker.save()

	return render(request, './take_dog.html', context)




def AboutView(request) :

	return render(request, './about_us.html')


def StatsView(request) :

	return render(request, './stats.html')


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



def result_dog(request) :

	select = []

	for i in range(1,8) :
		tmp = request.POST['question' + str(i)]
		select.append(tmp)

	print(select)

	data = {
		'result' : 'bichon'
	}

	return JsonResponse(data)



def register_marker(request) :

	#location_name = request.GET.get('location_name', None)
	#dog_name = request.GET.get('dog_name', None)
	#img_src = request.GET.get('image_src', None)
	#x = request.GET.get('x', None)
	#y = request.GET.get('y', None)
	#print(location_name, dog_name, img_src, x, y)
	#marker = Marker(location_name = location_name, x = x, y = y, dog_name = dog_name, img_src = img_src)
	#marker.save()

	#myfile = request.FILES['image']
	#fs = FileSystemStorage()
	#filename = fs.save(myfile.name, myfile)
	#uploaded_file_url = fs.url(filename)

	#print(uploaded_file_url)

	dn = request.POST.get('id_dog_name', False)
	print(dn)

	data = {
		'result' : 'success'
	}

	return JsonResponse(data)


def delete_marker(request) :

	pk_id = request.GET.get('pk_id', None)
	psw_txt = request.GET.get('psw_txt', None)

	print(psw_txt)

	query = Marker.objects.get(pk=pk_id)
	if(query.psw == psw_txt) :
		query.delete()

		data = {
			'result' : 'success'
		}
	else :
		data = {
			'result' : '비밀번호가 다릅니다.'
		}

	return JsonResponse(data)



def change_marker(request) :

	pk_id = request.GET.get('pk_id', None)
	psw_txt = request.GET.get('psw_txt', None)

	print(psw_txt)

	query = Marker.objects.get(pk=pk_id)
	if(query.psw == psw_txt) :
		data = {
			'result' : 'success'
		}
	else :
		data = {
			'result' : '비밀번호가 다릅니다.'
		}

	return JsonResponse(data)




def register_dog(request) :
	context = {}

	rp = request.path
	if len(rp) > 14 :
		pk_id = rp[14:]
		#print(pk_id)
		dog = Marker.objects.get(pk=pk_id)
		context['dog'] = dog
		#print(context)

	else :
		context['dog'] = None

	print(context)

	return render(request, './register_dog.html', context)


def take_register_dog(request) :
	context = {}

	rp = request.path
	if len(rp) > 19 :
		pk_id = rp[19:]
		#print(pk_id)
		dog = TakeMarker.objects.get(pk=pk_id)
		context['dog'] = dog
		#print(context)

	else :
		context['dog'] = None

	return render(request, './take_register_dog.html', context)