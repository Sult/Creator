from django.contrib import admin
from world.models import Country, Province, Region

class CountryAdmin(admin.ModelAdmin):
	fieldsets = [
		('Country', {'fields': ['name', 'flavor', 'history', 'approved', 'edited']}),
	]
	
	list_display = ('name', 'approved', 'edited')
	list_filter = ['approved']
	search_fields = ['name']

admin.site.register(Country, CountryAdmin)
