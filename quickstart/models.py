from django.db import models


class Table1(models.Model):
	choice1 = models.IntegerField(default=0)
	choice2 = models.IntegerField(default=0)
	name = models.CharField(max_length=300, default=" ")

class Table2(models.Model):
	rest_names= models.CharField(max_length=1000, default=" ")

class Table3(models.Model):
	loc_names= models.CharField(max_length=1000, default=" ")
	
	



