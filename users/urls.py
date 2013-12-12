from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
	url(r'^$', views.login_user, name='login_user'),
	url(r'^index/$', views.index, name='index'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^register/$', views.register_user, name='register_user'),
)

