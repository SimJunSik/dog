from django.db import models
from django.utils import timezone

# Create your models here.
class Breed(models.Model):
	name=models.CharField(max_length=50,default="unknown")
	k_name=models.CharField(max_length=50,default="unknown")
	size=models.CharField(max_length=50,default="unknown")
	temperament=models.CharField(max_length=500,default="unknown")
	apartment_friendliness=models.IntegerField(default=0)
	child_friendliness=models.IntegerField(default=0)
	cat_friendliness=models.IntegerField(default=0)
	dog_friendliness=models.IntegerField(default=0)
	grooming=models.IntegerField(default=0)
	face_type=models.CharField(max_length=50,default="unknown")
	fur=models.CharField(max_length=50,default="unknown")
	temp_group=models.CharField(max_length=50,default="unknown")
	result_cnt=models.IntegerField(default=0)
	rank=models.IntegerField(default=0)

	def __str__(self):
		return self.k_name

class Dog(models.Model) :

	name = models.CharField(max_length=20)

	def __str__(self) :
		return self.name


class User(models.Model) :

	id_str = models.CharField(max_length=20)

	psw_str = models.CharField(max_length=20)

	auth = models.IntegerField(default=1)

	def __str__(self) :
		return self.id_str


class Area(models.Model) :

	area_name = models.CharField(max_length=40, default = '')

	lost_cnt = models.IntegerField(default=0)

	take_cnt = models.IntegerField(default=0)
	
	def __str__(self) :

		return self.area_name



class Marker(models.Model) :

	location_name = models.CharField(max_length=200)

	dog_name = models.CharField(max_length=40, default='unknown')

	img_src = models.CharField(max_length=400, default='../../media/dog.png')

	created_at = models.DateField(default=timezone.now)

	losted_at = models.DateField(default=timezone.now)

	feature = models.CharField(max_length=1000, default='')

	phone = models.CharField(max_length=20, default='000-0000-000')

	reward = models.CharField(max_length=20, default='0000')

	#document = models.FileField(upload_to='documents/', default='documents/')
    #uploaded_at = models.DateTimeField(auto_now_add=True)

	x = models.FloatField(default=0.0)

	y = models.FloatField(default=0.0)

	psw = models.CharField(max_length=15, default='0000')

	def __str__(self) :
		return self.location_name



class TakeMarker(models.Model) :

	location_name = models.CharField(max_length=200)

	dog_name = models.CharField(max_length=40, default='unknown')

	img_src = models.CharField(max_length=400, default='../../media/dog.png')

	created_at = models.DateField(default=timezone.now)

	losted_at = models.DateField(default=timezone.now)

	feature = models.CharField(max_length=1000, default='')

	phone = models.CharField(max_length=20, default='000-0000-000')

	reward = models.CharField(max_length=20, default='0000')

	#document = models.FileField(upload_to='documents/', default='documents/')
    #uploaded_at = models.DateTimeField(auto_now_add=True)

	x = models.FloatField(default=0.0)

	y = models.FloatField(default=0.0)

	psw = models.CharField(max_length=15, default='0000')

	def __str__(self) :
		return self.location_name



class CompleteMarker(models.Model) :

	location_name = models.CharField(max_length=200)

	dog_name = models.CharField(max_length=40, default='unknown')

	img_src = models.CharField(max_length=400, default='../../media/dog.png')

	created_at = models.DateField(default=timezone.now)

	losted_at = models.DateField(default=timezone.now)

	feature = models.CharField(max_length=1000, default='')

	phone = models.CharField(max_length=20, default='000-0000-000')

	reward = models.CharField(max_length=20, default='0000')

	completed_at = models.DateField(default=timezone.now)

	#document = models.FileField(upload_to='documents/', default='documents/')
    #uploaded_at = models.DateTimeField(auto_now_add=True)

	x = models.FloatField(default=0.0)

	y = models.FloatField(default=0.0)

	psw = models.CharField(max_length=15, default='0000')

	def __str__(self) :
		return self.location_name




class Shelter(models.Model) :

	name = models.CharField(max_length=60, default='')

	addr = models.CharField(max_length=200, default='')

	num = models.CharField(max_length=60, default='')

	location = models.CharField(max_length=60, default='')

	def __str__(self) :
		return self.name