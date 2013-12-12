from django.db import models

from users.models import ModelLog

class Country(models.Model):
	"""
	Top layer of world elements,  has serveral provinces in it (max 4-8)
	"""
	
	name = models.CharField(max_length=127, unique=True)
	flavor = models.TextField()
	history = models.TextField()
	likes = models.ForeignKey('self', related_name='likes_country', null=True, blank=True)
	hates = models.ForeignKey('self', related_name='hates_country', null=True, blank=True)
	
	approved = models.BooleanField(default=False)						# Set to True when object is verrified/accepted
	log = models.OneToOneField(ModelLog, null=True, blank=True)
	edited = models.DateTimeField()
	
	class Meta:
		verbose_name = 'Countrie'
	
	
	def __unicode__(self):
		return self.name
	
	
class Province(models.Model):
	"""
	A big region within a country, containing several regions(
	"""
	
	country = models.ForeignKey(Country)
	
	name = models.CharField(max_length=127, unique=True)
	flavor = models.TextField()
	history = models.TextField()
	
	approved = models.BooleanField(default=False)						# Set to True when object is verrified/accepted
	log = models.OneToOneField(ModelLog, null=True, blank=True)
	edited = models.DateTimeField()
	
	def __unicode__(self):
		return self.name
	
	
class Region(models.Model):
	"""
	contains some towns (max 3?) villages, batle/farm sites and more
	"""
	
	province = models.ForeignKey(Province)
	
	name = models.CharField(max_length=127, unique=True)
	flavor = models.TextField()
	history = models.TextField()
	
	approved = models.BooleanField(default=False)						# Set to True when object is verrified/accepted
	log = models.OneToOneField(ModelLog, null=True, blank=True)
	edited = models.DateTimeField()
	
	def __unicode__(self):
		return self.name
