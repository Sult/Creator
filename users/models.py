from django.db import models
from django.contrib.auth.models import User

class ModelLog(models.Model):
	"""
	logging changed data of objects done by users manualy
	"""
	
	model = models.CharField(max_length=255)
	app = models.CharField(max_length=255)
	
	date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User)
	
	fields = models.TextField()
	
	old_data = models.TextField()
	new_data = models.TextField()
	
	def __unicode__(self):
		return "Model: %s, by: %s, at: %s" % (self.model, self.user, self.date)
	
	
	@staticmethod
	def create_log(user_obj, old_obj, new_obj):
		""" Create a log about the changes of an object"""
		
		the_model = old_obj.__class__.__name__
		the_app = str(old_obj.__class__._meta.app_label)
		the_user = user_obj

		# get all fields from model  fields = obj.__class__._meta.fields
		# Get attribute form object   obj.__getattribute__(fields[1].name)
		all_fields = old_obj.__class__._meta.fields
		
		changed_fields = ""
		the_old_data = ""
		the_new_data = ""
		count = 0
		
		if old_obj == new_obj:
			# New object created log
			for field in all_fields:
				new_field_data = new_obj.__getattribute__(field.name)
				changed_fields = "All"
				the_old_data = 'Created new object'
				the_new_data = the_new_data + str(new_field_data) + "     "
		
		# get all changed data
		else:
			for field in all_fields:
				old_field_data = old_obj.__getattribute__(field.name)
				
				# get all changed fields and convert them to string
				if old_field_data != new_field_data:
					count = count + 1
					# number + space + data + 5 spaces for next string
					changed_fields = changed_fields + str(count) + "." + str(field.name) + "     "
					the_old_data = the_old_data + str(count) + "." + str(old_field_data) + "     "
					the_new_data = the_new_data + str(count) + "." + str(new_field_data) + "     "
		
		
		new_log = ModelLog(
			model = the_model,
			app = the_app,
			user = the_user,
			fields = changed_fields,
			old_data = the_old_data,
			new_data = the_new_data,
		)
		new_log.save()
		
		return new_log
