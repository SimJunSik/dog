from django.db import models

# Create your models here.

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