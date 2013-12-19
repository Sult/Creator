from django.conf.urls import patterns, url

from world import views

urlpatterns = patterns('',
	url(r'^world/$', views.world, name='world'),
	
	# country related views
	url(r'^world/country/$', views.country, name='country'),
	url(r'^world/country/create/$', views.create_country, name='create_country'),
	url(r'^world/country/edit/(?P<country_id>\d+)/$', views.edit_country, name='edit_country'),
	url(r'^world/country/delete/(?P<country_id>\d+)/$', views.delete_country, name='delete_country'),
	
	# province related views
	url(r'^world/province/$', views.province, name='province'),
	url(r'^world/province/create/$', views.create_province, name='create_province'),
	url(r'^world/province/edit/(?P<province_id>\d+)/$', views.edit_province, name='edit_province'),
	url(r'^world/province/delete/(?P<province_id>\d+)/$', views.delete_province, name='delete_province'),
	
	# region related views
	url(r'^world/region/$', views.region, name='region'),
	
	#url(r'^logout/$', views.logout, name='logout'),
	#url(r'^register/$', views.register_user, name='register_user'),
	#url(r'^register_success/$', views.register_success, name='register_success'),
)
