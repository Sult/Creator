from django.contrib import admin
from world.models import Country, Province, Region

class CountryAdmin(admin.ModelAdmin):
	fieldsets = [
		('Country', {'fields': ['name', 'flavor', 'history', 'likes', 'hates', 'approved', 'log', 'edited']}),
	]
	
	list_display = ('name', 'likes', 'hates', 'approved', 'log', 'edited')
	list_filter = ['approved']
	search_fields = ['name']

admin.site.register(Country, CountryAdmin)
