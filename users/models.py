from django.db import models
from django.contrib.auth.models import User

import datetime
from django.utils.timezone import utc

class ModelLog(models.Model):
	"""
	logging changed data of objects done by users manualy
	"""
	
	pk = models.IntegerField()
	model = models.CharField(max_length=255)
	app = models.CharField(max_length=255)
	
	date = models.DateTimeField()
	user = models.ForeignKey(User)
	
	field_data = models.TextField()
	
	def __unicode__(self):
		return "Model: %s, by: %s, at: %s" % (self.model, self.user, self.date)
	
	
	@staticmethod
	def create_log(user_obj, obj):
		""" Create a log about the changes of an object"""
		
		the_model = obj.__class__.__name__
		the_app = str(obj.__class__._meta.app_label)
		the_user = user_obj
		the_date = datetime.datetime.utcnow().replace(tzinfo=utc)
		
		# get all fields from model  fields = obj.__class__._meta.fields
		# Get attribute form object   obj.__getattribute__(fields[1].name)
		all_fields = obj.__class__._meta.fields
		
		the_pk = obj.__getattribute__(all_fields[0].name)
		
		the_field_data = ""
		
		# get all changed data
		
		for field in all_fields:
			data =obj.__getattribute__(field.name)
			
			# field name - data - new line
			the_field_data = the_field_data + str(field.name) + ": " + str(data) + "\n"
			
		new_log = ModelLog(
			pk = the_pk,
			model = the_model,
			app = the_app,
			user = the_user,
			date = the_date,
			field_data = the_field_data,
		)
		new_log.save()
