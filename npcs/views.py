from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf

from users.models import ModelLog
from npcs.models import Faction, NPCGuild
from npcs.forms import FactionForm, NPCGuildForm

import datetime
from django.utils.timezone import utc

# NPC Overview tyhat shows some last edited objects and opens up the submenu (later javascript)
def npc(request):
	# Check if user is logged in
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login_user'))
	
	#list last edited objects
	factions = Faction.objects.order_by('-edited')[:3]
	npc_guilds = NPCGuild.objects.order_by('-edited')[:5]
	
	return render(request, 'npcs.html', {'factions': factions, 'npc_guilds': npc_guilds})


# (NPC) Factions, overview and objects that need attention
def faction(request):
	# Check if user is logged in
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login_user'))
	
	# List all countries in table with basic information
	factions = Faction.objects.order_by('name')
	
	messages = []
	for faction in factions:
		messages.append(Faction.need_attention(faction))
	
	return render(request, 'faction.html', {'factions': factions, 'messages': messages})


# Create a new Faction
def create_faction(request):
	# Check if user is logged in
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login_user'))
	
	form_url = "create"
	
	if request.POST:
		faction_form = FactionForm(request.POST)
		if faction_form.is_valid():
			new_faction = faction_form.save(commit=False)
			new_faction.edited = datetime.datetime.utcnow().replace(tzinfo=utc)
			new_faction.save()
			ModelLog.create_log(request.user, new_faction)
			
			return HttpResponseRedirect(reverse('faction'))
			
		else:
			return render(request, 'create_faction.html', {'faction_form': faction_form, 'form_url': form_url})
				
	faction_form = FactionForm() 
	
	return render(request, 'create_faction.html', {'faction_form': faction_form, 'form_url': form_url})
	

# edit a faction
def edit_faction(request, faction_id):
	# check if user is logged in
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login_user'))
		
	faction = get_object_or_404(Faction, pk=faction_id)
	form_url = "edit"
	
	faction_form = FactionForm(request.POST or None, instance=faction)
	if faction_form.is_valid():
		edit_faction = faction_form.save(commit=False)
		edit_faction.edited = datetime.datetime.utcnow().replace(tzinfo=utc)
		edit_faction.save()
		ModelLog.create_log(request.user, edit_faction)
		
		return HttpResponseRedirect(reverse('faction'))
			
	return render(request, 'create_faction.html', {'faction_form': faction_form, 'form_url': form_url, 'faction_id': faction.id})
	

# Delete a faction	
def delete_faction(request, faction_id):
	# check if user is logged in
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login_user'))
	
	delete_faction = get_object_or_404(Faction, pk=faction_id)
	
	if request.POST:
		ModelLog.create_log(request.user, delete_faction)
		delete_faction.delete()
		return HttpResponseRedirect(reverse('faction'))
	
	return render(request, 'delete_faction.html',{'delete_faction': delete_faction})
	

# NPC Guild Overview
def npc_guild(request):
	# Check if user is logged in
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login_user'))
	
	# List all countries in table with basic information
	npc_guilds = NPCGuild.objects.order_by('name')
	
	messages = []
	for npc_guild in npc_guilds:
		messages.append(NPCGuild.need_attention(npc_guild))
	
	return render(request, 'npc_guild.html', {'npc_guilds': npc_guilds, 'messages': messages})


# Create a new NPC Guild
def create_npc_guild(request):
	# Check if user is logged in
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login_user'))
	
	form_url = "create"
	
	if request.POST:
		npc_guild_form = NPCGuildForm(request.POST)
		if npc_guild_form.is_valid():
			new_npc_guild = npc_guild_form.save(commit=False)
			new_npc_guild.edited = datetime.datetime.utcnow().replace(tzinfo=utc)
			new_npc_guild.save()
			ModelLog.create_log(request.user, new_npc_guild)
			return HttpResponseRedirect(reverse('npc_guild'))			
		else:
			return render(request, 'create_npc_guild.html', {'npc_guild_form': npc_guild_form, 'form_url': form_url})
				
	npc_guild_form = NPCGuildForm() 
	return render(request, 'create_npc_guild.html', {'npc_guild_form': npc_guild_form, 'form_url': form_url})


# Edit a NPC Guild
def edit_npc_guild(request, npc_guild_id):
	# check if user is logged in
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login_user'))
		
	npc_guild = get_object_or_404(NPCGuild, pk=npc_guild_id)
	form_url = "edit"
	
	npc_guild_form = NPCGuildForm(request.POST or None, instance=npc_guild)
	if npc_guild_form.is_valid():
		edit_npc_guild = npc_guild_form.save(commit=False)
		edit_npc_guild.edited = datetime.datetime.utcnow().replace(tzinfo=utc)
		edit_npc_guild.save()
		ModelLog.create_log(request.user, edit_npc_guild)
		
		return HttpResponseRedirect(reverse('npc_guild'))
			
	return render(request, 'create_npc_guild.html', {'npc_guild_form': npc_guild_form, 'form_url': form_url, 'npc_guild_id': npc_guild.id})
	

# Delete a NPC Guild
def delete_npc_guild(request, npc_guild_id):
	# check if user is logged in
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login_user'))
	
	delete_npc_guild = get_object_or_404(NPCGuild, pk=npc_guild_id)
	
	if request.POST:
		ModelLog.create_log(request.user, delete_npc_guild)
		delete_npc_guild.delete()
		return HttpResponseRedirect(reverse('npc_guild'))
	
	return render(request, 'delete_npc_guild.html',{'delete_npc_guild': delete_npc_guild})
