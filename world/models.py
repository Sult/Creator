from django.db import models

from users.models import ModelLog

class Country(models.Model):
	"""
	Top layer of world elements,  has serveral provinces in it (max 4-8)
	"""

	
	name = models.CharField(max_length=127, unique=True)
	flavor = models.TextField()
	history = models.TextField()
	approved = models.BooleanField(default=False)						# Set to True when object is verrified/accepted
	edited = models.DateTimeField()
	
	
	
	def __unicode__(self):
		return self.name
	
	
class Province(models.Model):
	"""
	A big region within a country, containing several regions(
	"""
	
	country = models.ForeignKey(
				Country, 
				null=True,
				blank=True,
				on_delete=models.SET_NULL
				)
	
	name = models.CharField(max_length=127, unique=True)
	flavor = models.TextField()
	history = models.TextField()
	approved = models.BooleanField(default=False)						# Set to True when object is verrified/accepted
	edited = models.DateTimeField()
	
	@staticmethod
	def need_attention(obj):
		"""
		checkes what objects are not ready to be approved yet
		They have missing fields or other points that need attention
		"""

		if obj.country == None:
			message = [obj]
			message.append("province should be linked to a country")
			return message
	
	def __unicode__(self):
		return self.name
	
	
class Region(models.Model):
	"""
	contains some towns (max 3?) villages, batle/farm sites and more
	"""
	
	province = models.ForeignKey(
				Province, 
				null=True, 
				on_delete=models.SET_NULL
				)
		
	name = models.CharField(max_length=127, unique=True)
	flavor = models.TextField()
	history = models.TextField()
	approved = models.BooleanField(default=False)						# Set to True when object is verrified/accepted
	edited = models.DateTimeField()
	
	def __unicode__(self):
		return self.name
