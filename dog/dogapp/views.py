from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.core import serializers
import json
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

def DogCrawling(request) :
	import sys, os
	from django.conf import settings
	import codecs
	from bs4 import BeautifulSoup
	import urllib.request
	from urllib.parse import quote
	from urllib.request import Request, urlopen
	from django.shortcuts import render_to_response
	import urllib
	import csv


	
	a = 'http://www.dogbreedslist.info/all-dog-breeds/'
	b = 'list_1_'
	c = '.html#.WiK_Tkpl-Uk'
	cnt = 0
	href_list = []

	f = open('dogapp/result.csv', 'w', encoding='utf-8', newline='')
	wr = csv.writer(f)



	for num in range(1, 20) :

		result = a + b + str(num) + c
		html = urllib.request.urlopen(result)
		soup = BeautifulSoup(html, 'lxml')

		link = soup.find_all("div", {"class" : "left"})
		for m in link :
			if(m.find("a")) :
				try:
					#print(m.a.get('href'))
					href_list.append(m.a.get('href'))
				except :
					continue

	#print(cnt)

	needs_list = ['Name', 'Size', 'Temperament', 'Grooming', 'Apartment Friendly', 'Child Friendly', 'Cat Friendly', 'Dog Friendly']
	needs_list2 = ['Name']
	wr.writerow(needs_list)


	for num in href_list :
		#f = open('dogapp/result2.txt', 'a+')

		html = urllib.request.urlopen(num)
		soup = BeautifulSoup(html, 'lxml')

		link = soup.find("table", {"class" : "table-01"})

		items = link.find_all("td")

		cnt = cnt+1
		#print("NUMBER :: " + str(cnt))
		print(cnt)
		tmp_content = []
		#f.write("NUMBER :: " + str(cnt) + "\n")
		for item in items :
			#print(item.get_text())
			for i in needs_list :
				if(item.get_text() == i) :
					#print("**** " + item.get_text() + " ****")
					#f.write("**** " + item.get_text() + " ****"  + "\n")

					#print(items[items.index(item)+1])
					for string in items[items.index(item)+1] :
						if(str(string)[0] == '<') :
							tmp = ''
							idx1 = 0
							idx2 = 0
							tmp_string = str(string).replace("<", "", 1)
							for char in tmp_string :
								if(char == '>') :
									idx1 = str(tmp_string).index(char)

								if(char == '<') :
									idx2 = str(tmp_string).index(char)

							tmp = str(tmp_string)[idx1+1:idx2]
							#print(tmp)
							try :
								#print(tmp)
								#f.write(tmp  + "\n")
								tmp_content.append(tmp)
								#wr.writerow(tmp_content)
								if(item.get_text() == 'Grooming' or 
									item.get_text() == 'Apartment Friendly' or 
									item.get_text() == 'Child Friendly' or 
									item.get_text() == 'Cat Friendly' or
									item.get_text() == 'Dog Friendly') :
									break
							except :
								print('aa')
								tmp_content.append(str(string))
								#wr.writerow(tmp_content)
								#f.write("!!!!!!!!wrtie error\n")
						else :
							#print(str(string))
							try :
								#print(str(string))
								tmp_content.append(str(string))
								#wr.writerow(tmp_content)
							except :
								print("bb")
								#wr.writerow(tmp_content)
								#f.write("!!!!!!!!wrtie error\n")
		#print(tmp_content)
		wr.writerow(tmp_content)
		#f.write("\n\n")
						
								

	f.close()

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

def UpdateData(request) :
	json_serializer = serializers.get_serializer("json")()
	dogs = json_serializer.serialize(Marker.objects.all(), ensure_ascii=False)

	data = {
		'dogs' : dogs
	}


	return JsonResponse(data)


def UpdateData2(request) :

	json_serializer = serializers.get_serializer("json")()
	dogs = json_serializer.serialize(TakeMarker.objects.all(), ensure_ascii=False)

	data = {
		'dogs' : dogs
	}


	return JsonResponse(data)


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

	if request.method == 'POST':
		file_get = request.POST.get('dog_image', False)
		if(file_get == False) :
			img_src = request.FILES['dog_image']
			fs = FileSystemStorage()
			filename = fs.save(img_src.name, img_src)
			uploaded_file_url = fs.url(filename)
			#print(uploaded_file_url)

		location_name = request.POST.get('location_name')

		area_name = location_name.split(' ')[1]

		#print(area_name)

		query = Area.objects.get(area_name = area_name)
		query.lost_cnt = query.lost_cnt + 1
		query.save()

		#print(location_name)
		lat = request.POST.get('lat')
		lng = request.POST.get('lng')
		#print(lat, lng)
		dog_name = request.POST.get('dog_name')
		psw_txt = request.POST.get('psw_txt')
		#print(location_name, lat, lng)
		losted_at = request.POST.get('losted_at')

		feature = request.POST.get('feature')

		phone = request.POST.get('phone')

		reward = request.POST.get('reward')

		pk_value = request.POST.get('pk_value')
		#print(pk_value)
		if pk_value == 'none'  or len(pk_value)==0 :
			marker = Marker(location_name = location_name, 
							x = lat, 
							y = lng, 
							dog_name = dog_name, 
							img_src = uploaded_file_url, 
							psw = psw_txt, 
							losted_at = losted_at, 
							feature = feature,
							phone = phone,
							reward = reward)
			marker.save()
		else :
			marker = Marker.objects.get(pk=pk_value)
			marker.location_name = location_name
			marker.x = lat
			marker.y = lng
			marker.dog_name = dog_name
			marker.psw = psw_txt
			marker.losted_at = losted_at
			makker.feature = feature
			marker.phone = phone
			marker.reward = reward
			if(file_get == False) :
				marker.img_src = uploaded_file_url
			marker.save()

	dogs = Marker.objects.all()
	markers = json_serializer.serialize(dogs, ensure_ascii=False)

	context = {'markers' : markers, 'dogs' : dogs}

	return render(request, './notice_test.html', context)



def TakedogView(request) :

	json_serializer = serializers.get_serializer("json")()

	if request.method == 'POST':
		file_get = request.POST.get('dog_image', False)
		if(file_get == False) :
			img_src = request.FILES['dog_image']
			fs = FileSystemStorage()
			filename = fs.save(img_src.name, img_src)
			uploaded_file_url = fs.url(filename)
			#print(uploaded_file_url)

		location_name = request.POST.get('location_name')

		area_name = location_name.split(' ')[1]

		#print(area_name)

		query = Area.objects.get(area_name = area_name)
		query.take_cnt = query.take_cnt + 1
		query.save()
		
		#print(location_name)
		lat = request.POST.get('lat')
		lng = request.POST.get('lng')
		#print(lat, lng)
		dog_name = request.POST.get('dog_name')
		psw_txt = request.POST.get('psw_txt')
		#print(location_name, lat, lng)
		losted_at = request.POST.get('losted_at')

		feature = request.POST.get('feature')

		phone = request.POST.get('phone')

		pk_value = request.POST.get('pk_value')
		#print(pk_value)
		if pk_value == 'none'  or len(pk_value)==0 :
			marker = TakeMarker(location_name = location_name, 
								x = lat, 
								y = lng, 
								dog_name = dog_name, 
								img_src = uploaded_file_url, 
								psw = psw_txt, 
								losted_at = losted_at, 
								feature = feature,
								phone = phone)
			marker.save()
		else :
			marker = TakeMarker.objects.get(pk=pk_value)
			marker.location_name = location_name
			marker.x = lat
			marker.y = lng
			marker.dog_name = dog_name
			marker.psw = psw_txt
			marker.losted_at = losted_at
			makker.feature = feature
			marker.phone = phone
			if(file_get == False) :
				marker.img_src = uploaded_file_url
			marker.save()

	dogs = TakeMarker.objects.all()
	markers = json_serializer.serialize(dogs, ensure_ascii=False)

	context = {'markers' : markers, 'dogs' : dogs}

	return render(request, './take_dog.html', context)



def CompleteDogView(request) :

	dogs = CompleteMarker.objects.all()

	context = {'dogs' : dogs}

	return render(request, './complete_dog.html', context)



def DonatorView(request) :

	return render(request, './donator.html')


def AboutView(request) :

	return render(request, './about_us.html')


def StatsView(request) :

	return render(request, './stats.html')


def MembershipView(request) :

	return render(request, './membership.html')

def MatchingView(request) :

	return render(request, './matching.html')




def MatchingResultView(request) :

	select = []
	select_str = ''
	is_not_shared=True
	no_room=False
	too_lazy=False

	rp = request.path
	#print(rp)

	if len(rp) > 17 :
		#print(rp[17:])
		for item in rp[17:] :
			select.append(item)
			select_str = select_str + str(item)
		is_not_shared=False
		#print(select)

	else :
		for i in range(1,8) :
			tmp = request.POST['question' + str(i)]
			select.append(tmp)
			select_str = select_str + str(tmp)

		#print(select)

	#print(select_str)

# 가족구성원: 1인/2인/아이/부모님/3대
# 집형태: 마당/넓은아파트/좁은아파트/원룸 및 오피스텔
# 설거지: 쌓아둔다/바로바로한다/만들지않는다
# 연예인상: 강아지/고양이/곰상 
# 이상형: 지적인/애교많은/사교적인/해바라기/듬직한
	
# size/temperament/aparmtent_friendliness/child_friendliness/grooming
	no_recommendation=False

	child_friendliness=0
	cat_friendliness=0
	dog_friendliness=0
	apartment_friendliness=0
	grooming=0
	fur=""
	temperament=0
	size=""
	face_type=""
	temper_group=[]

# 가족구성원: 고양이/강아지/아이/해당없음
	if(select[0]=="1"):
		cat_friendliness=3
	elif(select[0]=="2"):
		dog_friendliness=3
	elif(select[0]=="3"):
		child_friendliness=5

# 집형태: 마당/넓은아파트/좁은아파트/원룸 및 오피스텔
	if(select[1]=="1"):
		apartment_friendliness=1
	elif(select[1]=="2"):
		apartment_friendliness=2
	elif(select[1]=="3"):
		apartment_friendliness=4
	elif(select[1]=="4"):
		apartment_friendliness=5
		no_room=True

# 설거지: 쌓아둔다/바로바로한다/만들지않는다
	if(select[2]=='1'):
		grooming=3
	elif(select[2]=='2'):
		grooming=5
	elif(select[2]=='3'):
		grooming=1
		
# 연예인상: 강아지 /고양이/곰상/공룡
	if(select[3]=='1'):
		face_type="강아지"
	elif(select[3]=='2'):
		face_type="고양이"
	elif(select[3]=='3'):
		face_type="곰상"
	elif(select[3]=='4'):
		face_type="공룡"
	# elif(select[3]=='5'):
	# 	face_type="여우"

# 이상형: 지적인/애교많은/사교적인/해바라기/듬직한
	if(select[4]=='1'):
		temperament=1
	elif(select[4]=='2'):
		temperament=2
	elif(select[4]=='3'):
		temperament=3
	elif(select[4]=='4'):
		temperament=4
	elif(select[4]=='5'):
		temperament=5
	
# 머리스타일: 곱슬/ 단모/ 장모
	if(select[5]=='1'):
		fur="곱슬"
	elif(select[5]=='2'):
		fur="단모"
	elif(select[5]=='3'):
		fur="장모"

# 사이즈: s/m/l/g
	if(select[6]=='1'):
		size='Small'
	elif(select[6]=='2'):
		size="Medium"
	elif(select[6]=='3'):
		size="Large"
	elif(select[6]=='4'):
		size="Giant"

	result = []

	
	for breed in Breed.objects.all():
		if( int(breed.child_friendliness)>=int(child_friendliness) 
			and int(breed.apartment_friendliness)>=int(apartment_friendliness) 
			and int(breed.cat_friendliness)>=int(cat_friendliness) 
			and int(breed.dog_friendliness)>=int(dog_friendliness)
			and int(breed.grooming)<=int(grooming)
			and breed.face_type==face_type
			and breed.fur==fur
			and size in breed.size
			and str(temperament) in breed.temp_group
			):
				#data['result']+="\n"+breed.name
				#data['k_result'] += "\n"+breed.k_name
				result.append(breed)
				if is_not_shared :
					breed.result_cnt = breed.result_cnt + 1
					breed.save()
	
	if not result :
		for breed in Breed.objects.all():

			if( int(breed.child_friendliness)>=int(child_friendliness)
				and int(breed.apartment_friendliness)>=int(apartment_friendliness)
				and int(breed.cat_friendliness)>=int(cat_friendliness)
				and int(breed.dog_friendliness)>=int(dog_friendliness)
				and int(breed.grooming)<=int(grooming)
				and breed.fur==fur
				and str(temperament) in breed.temp_group
				):
					#data['result']+="\n"+breed.name
					#data['k_result'] += "\n"+breed.k_name
					result.append(breed)
					if is_not_shared :
						breed.result_cnt = breed.result_cnt + 1
						breed.save()

	if not result :
		for breed in Breed.objects.all():

			if( int(breed.child_friendliness)>=int(child_friendliness)
				and int(breed.apartment_friendliness)>=int(apartment_friendliness)
				and int(breed.cat_friendliness)>=int(cat_friendliness)-1
				and int(breed.dog_friendliness)>=int(dog_friendliness)-1			
				and int(breed.grooming)<=int(grooming)
				):
					#data['result']+="\n"+breed.name
					#data['k_result'] += "\n"+breed.k_name
					result.append(breed)
					if is_not_shared :
						breed.result_cnt = breed.result_cnt + 1
						breed.save()

	for item in result :
		if " " in item.name :
			item.name = item.name.replace(" ", "-")
		else :
			item.name = item.name

	#지적인/애교많은/사교적인/해바라기/듬직한
		item.temp_group = item.temp_group.replace("[", "")
		item.temp_group = item.temp_group.replace("]", "")
		item.temp_group = item.temp_group.replace(",", "")
		item.temp_group = item.temp_group.replace(" ", "")
		item.temp_group = item.temp_group.replace("'", "")

		tmp = item.temp_group
		#print(item.temp_group)
		item.temp_group = []
		for t in tmp :
			if t=='1' :
				item.temp_group.append('지적인')
			if t=='2' :
				item.temp_group.append('애교많은')
			if t=='3' :
				item.temp_group.append('사교적인')
			if t=='4' :
				item.temp_group.append('해바라기')
			if t=='5' :
				item.temp_group.append('듬직한')	

		#print(item.temp_group)


	#print(select_str[4])
	select_4 = ''
	if select_str[4] == '1' :
		select_4 = '지적인'
	if select_str[4] == '2' :
		select_4 = '애교많은'
	if select_str[4] == '3' :
		select_4 = '사교적인'
	if select_str[4] == '4' :
		select_4 = '해바라기같은'
	if select_str[4] == '5' :
		select_4 = '듬직한'

	context = { 'results' : result , 'select_str' : select_str, 'select_4' : select_4}


	return render(request, './matching_result.html', context)






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
	no_room=False
	too_lazy=False

	for i in range(1,8) :
		tmp = request.POST['question' + str(i)]
		select.append(tmp)

# 가족구성원: 1인/2인/아이/부모님/3대
# 집형태: 마당/넓은아파트/좁은아파트/원룸 및 오피스텔
# 설거지: 쌓아둔다/바로바로한다/만들지않는다
# 연예인상: 강아지/고양이/곰상 
# 이상형: 지적인/애교많은/사교적인/해바라기/듬직한
	
# size/temperament/aparmtent_friendliness/child_friendliness/grooming
	no_recommendation=False

	child_friendliness=0
	cat_friendliness=0
	dog_friendliness=0
	apartment_friendliness=0
	grooming=0
	fur=""
	temperament=0
	size=""
	face_type=""
	temper_group=[]

# 가족구성원: 고양이/강아지/아이/해당없음
	if(select[0]=="1"):
		cat_friendliness=3
	elif(select[0]=="2"):
		dog_friendliness=3
	elif(select[0]=="3"):
		child_friendliness=5

# 집형태: 마당/넓은아파트/좁은아파트/원룸 및 오피스텔
	if(select[1]=="1"):
		apartment_friendliness=1
	elif(select[1]=="2"):
		apartment_friendliness=2
	elif(select[1]=="3"):
		apartment_friendliness=4
	elif(select[1]=="4"):
		apartment_friendliness=5
		no_room=True

# 설거지: 쌓아둔다/바로바로한다/만들지않는다
	if(select[2]=='1'):
		grooming=3
	elif(select[2]=='2'):
		grooming=5
	elif(select[2]=='3'):
		grooming=1
		
# 연예인상: 강아지 /고양이/곰상/공룡
	if(select[3]=='1'):
		face_type="강아지"
	elif(select[3]=='2'):
		face_type="고양이"
	elif(select[3]=='3'):
		face_type="곰상"
	elif(select[3]=='4'):
		face_type="공룡"
	# elif(select[3]=='5'):
	# 	face_type="여우"

# 이상형: 지적인/애교많은/사교적인/해바라기/듬직한
	if(select[4]=='1'):
		temperament=1
	elif(select[4]=='2'):
		temperament=2
	elif(select[4]=='3'):
		temperament=3
	elif(select[4]=='4'):
		temperament=4
	elif(select[4]=='5'):
		temperament=5
	
# 머리스타일: 곱슬/ 단모/ 장모
	if(select[5]=='1'):
		fur="곱슬"
	elif(select[5]=='2'):
		fur="단모"
	elif(select[5]=='3'):
		fur="장모"

# 사이즈: s/m/l/g
	if(select[6]=='1'):
		size='Small'
	elif(select[6]=='2'):
		size="Medium"
	elif(select[6]=='3'):
		size="Large"
	elif(select[6]=='4'):
		size="Giant"

	data = {
		'result' : '',
		'k_result' : ''
	}

	
	for breed in Breed.objects.all():
		if( int(breed.child_friendliness)>=int(child_friendliness) 
			and int(breed.apartment_friendliness)>=int(apartment_friendliness) 
			and int(breed.cat_friendliness)>=int(cat_friendliness) 
			and int(breed.dog_friendliness)>=int(dog_friendliness)
			and int(breed.grooming)<=int(grooming)
			and breed.face_type==face_type
			and breed.fur==fur
			and size in breed.size
			and str(temperament) in breed.temp_group
			):
				data['result']+="\n"+breed.name
				data['k_result'] += "\n"+breed.k_name
				breed.result_cnt = breed.result_cnt + 1
				breed.save()
	
	if data['result']=='':
		for breed in Breed.objects.all():

			if( int(breed.child_friendliness)>=int(child_friendliness)
				and int(breed.apartment_friendliness)>=int(apartment_friendliness)
				and int(breed.cat_friendliness)>=int(cat_friendliness)
				and int(breed.dog_friendliness)>=int(dog_friendliness)
				and int(breed.grooming)<=int(grooming)
				and breed.fur==fur
				and str(temperament) in breed.temp_group
				):
					data['result']+="\n"+breed.name
					data['k_result'] += "\n"+breed.k_name
					breed.result_cnt = breed.result_cnt + 1
					breed.save()

	if data['result']=='':
		for breed in Breed.objects.all():

			if( int(breed.child_friendliness)>=int(child_friendliness)
				and int(breed.apartment_friendliness)>=int(apartment_friendliness)
				and int(breed.cat_friendliness)>=int(cat_friendliness)-1
				and int(breed.dog_friendliness)>=int(dog_friendliness)-1			
				and int(breed.grooming)<=int(grooming)
				):
					data['result']+="\n"+breed.name
					data['k_result'] += "\n"+breed.k_name
					breed.result_cnt = breed.result_cnt + 1
					breed.save()
					
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
	#print(dn)

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


def complete_marker(request) :

	pk_id = request.GET.get('pk_id', None)
	take_pk_id = request.GET.get('take_pk_id', None)
	psw_txt = request.GET.get('psw_txt', None)

	print(psw_txt)
	if pk_id != None :
		query = Marker.objects.get(pk=pk_id)
	else :
		query = TakeMarker.objects.get(pk=take_pk_id)

	if(query.psw == psw_txt) :
		complete_marker = CompleteMarker(location_name = query.location_name, 
										x = query.x, 
										y = query.y, 
										dog_name = query.dog_name, 
										img_src = query.img_src, 
										psw = query.psw, 
										losted_at = query.losted_at, 
										feature = query.feature,
										phone = query.phone,
										reward = query.reward)
		complete_marker.save()
		query.delete()
		data = {
			'result' : 'success'
		}
	else :
		data = {
			'result' : '비밀번호가 다릅니다.'
		}

	return JsonResponse(data)



def sort_by_search(request) :

	dog_name = request.GET.get('dog_name', None)
	phone = request.GET.get('dog_phone', None)

	pk_list = []

	if dog_name != None :
		querys = Marker.objects.filter(dog_name = dog_name)

	if dog_name == None :
		querys = Marker.objects.filter(phone = phone)

	if dog_name != None and phone != None :
		querys = Marker.objects.filter(dog_name = dog_name, phone = phone)

	for query in querys :
		pk_list.append(query.pk)

	data = {
		'pk_list' : pk_list
	}

	return JsonResponse(data)



def sort_by_search_take(request) :

	dog_name = request.GET.get('dog_name', None)
	phone = request.GET.get('dog_phone', None)

	pk_list = []

	if dog_name != None :
		querys = TakeMarker.objects.filter(dog_name = dog_name)

	if dog_name == None :
		querys = TakeMarker.objects.filter(phone = phone)

	if dog_name != None and phone != None :
		querys = TakeMarker.objects.filter(dog_name = dog_name, phone = phone)

	for query in querys :
		pk_list.append(query.pk)

	data = {
		'pk_list' : pk_list
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



def show_info(request) :

	pk_id = request.GET.get('pk_id', None)
	take_pk_id = request.GET.get('take_pk_id', None)
	#print(pk_id , take_pk_id)
	if(pk_id != None) :
		marker = Marker.objects.get(pk=pk_id)
		reward = marker.reward

	else :
		marker = TakeMarker.objects.get(pk=take_pk_id)
		reward = None
	
	location_name = marker.location_name
	dog_name = marker.dog_name
	img_src = marker.img_src
	losted_at = marker.losted_at
	created_at = marker.created_at
	feature = marker.feature
	phone = marker.phone

	data = {
			'location_name' : location_name,
			'dog_name' : dog_name,
			'img_src' : img_src,
			'losted_at' : losted_at,
			'created_at' : created_at,
			'feature' : feature,
			'phone' : phone,
			'reward' : reward
		}

	return JsonResponse(data)


def add_rank(request) :

	import openpyxl
	excel_document = openpyxl.load_workbook('dog_result.xlsx')
	sheet = excel_document.get_sheet_by_name('result')

	cnt = 0
	for row in sheet.rows:
		cnt = cnt+1
		if(row[0].value=="Name"):
			continue
		newbreed=Breed()
		newbreed.name=row[0].value
		newbreed.grooming=str(row[1].value)[0]
		newbreed.apartment_friendliness=str(row[2].value)[0]
		newbreed.child_friendliness=str(row[3].value)[0]
		newbreed.cat_friendliness=str(row[4].value)[0]
		newbreed.dog_friendliness=str(row[5].value)[0]
		newbreed.temperament=str(row[6].value).split(',')
		newbreed.size=str(row[7].value).split(' to ')
		newbreed.face_type=row[8].value
		newbreed.fur=row[9].value
		newbreed.temp_group=row[10].value
		newbreed.k_name=row[11].value
		newbreed.rank=cnt
		newbreed.save()


	return render(request, './tmp.html')


# python manage.py shell에서 아래 입력 (DB)

# from dogapp.models import *
# import openpyxl
# excel_document = openpyxl.load_workbook('dog_result.xlsx')
# sheet = excel_document.get_sheet_by_name('result')



# for row in sheet.rows:
#     if(row[0].value=="Name"):
#         continue
#     newbreed=Breed()
#     newbreed.name=row[0].value
#     newbreed.grooming=str(row[1].value)[0]
#     newbreed.apartment_friendliness=str(row[2].value)[0]
#     newbreed.child_friendliness=str(row[3].value)[0]
#     newbreed.cat_friendliness=str(row[4].value)[0]
#     newbreed.dog_friendliness=str(row[5].value)[0]
#     newbreed.temperament=str(row[6].value).split(',')
#     newbreed.size=str(row[7].value).split(' to ')
#     newbreed.face_type=row[8].value
#     newbreed.fur=row[9].value
#     newbreed.temp_group=row[10].value
#     newbreed.k_name=row[11].value
#     newbreed.save()