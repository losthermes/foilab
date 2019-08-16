from django.db import models


#--------------- (LAB MODELS) ----------------

class Fuel(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.name

class Test(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.name

class Package(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	tests = models.ManyToManyField(Test,  blank=True)

	def __str__(self):
		return self.name



# --------------- (USER MODELS) ----------------
class Customer(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	company = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.name

class Sample(models.Model):
	customer =  models.ForeignKey(Customer,on_delete= models.CASCADE, blank=False, null=True)
	sample_id = models.CharField(max_length=200, null=True, blank=True)
	package = models.CharField(max_length=200, null=True, blank=True)
	Fuel = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.sample_id

class SampleTest(models.Model):
	sample =  models.ForeignKey(Sample,on_delete= models.CASCADE, blank=False, null=True)
	name = models.CharField(max_length=200, null=True, blank=True) 
	result = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.name


    