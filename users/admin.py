from django.contrib import admin
from users.models import ModelLog

class ModelLogAdmin(admin.ModelAdmin):
	fieldsets = [
		('Object info', {'fields': ['app', 'model', 'pk', 'user']}),
		('Changes', {'fields': ['field_data']}),
	]
	
	list_display = ('model', 'app', 'user', 'date')
	list_filter = ['app']
	search_fields = ('model', 'app', 'user')

admin.site.register(ModelLog, ModelLogAdmin)

