from django.conf.urls import patterns, url

from npcs import views

urlpatterns = patterns('',
	url(r'^npc/$', views.npc, name='npc'),
	
	# faction related views
	url(r'^npcs/faction/$', views.faction, name='faction'),
	url(r'^npcs/faction/create/$', views.create_faction, name='create_faction'),
	url(r'^npcs/faction/edit/(?P<faction_id>\d+)/$', views.edit_faction, name='edit_faction'),
	url(r'^npcs/faction/delete/(?P<faction_id>\d+)/$', views.delete_faction, name='delete_faction'),

	# NPC guilds related views
	url(r'^npcs/npc_guild/$', views.npc_guild, name='npc_guild'),
	url(r'^npcs/npc_guild/create/$', views.create_npc_guild, name='create_npc_guild'),
	url(r'^npcs/npc_guild/edit/(?P<npc_guild_id>\d+)/$', views.edit_npc_guild, name='edit_npc_guild'),
	url(r'^npcs/npc_guild/delete/(?P<npc_guild_id>\d+)/$', views.delete_npc_guild, name='delete_npc_guild'),
)
