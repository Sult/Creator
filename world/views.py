from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf

from users.models import ModelLog
from world.models import Country, Province, Region
from world.forms import CountryForm, ProvinceForm, RegionForm

import datetime
from django.utils.timezone import utc


def world(request):
	# Check if user is logged in
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login_user'))
	
	# show 3 last new/changed countries
	# show 3 last new/changed provinces
	# show 3 last new/changed regions
	
	return render(request, 'world.html')


def country(request):
	# Check if user is logged in
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login_user'))
	
	# List all countries in table with basic information
	countries = Country.objects.order_by('name')
	
	return render(request, 'country.html', {'countries': countries})

# create a new Country

def create_country(request):
	# check if user is logged in
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login_user'))
	
	form_url = "create"
	
	if request.POST:
		country_form = CountryForm(request.POST)
		if country_form.is_valid():
			new_country = country_form.save(commit=False)
			new_country.edited = datetime.datetime.utcnow().replace(tzinfo=utc)
			new_country.log = ModelLog.create_log(request.user, new_country, new_country)
			new_country.save()
			
			return HttpResponseRedirect(reverse('country'))
			
		else:
			return render(request, 'create_country.html', {'country_form': country_form, 'form_url': form_url})
				
	country_form = CountryForm() 
	
	return render(request, 'create_country.html', {'country_form': country_form, 'form_url': form_url})
	
	
# edit a already existing country
def edit_country(request, country_id):
	# check if user is logged in
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login_user'))
		
	country = get_object_or_404(Country, pk=country_id)
	form_url = "edit"
	
	country_form = CountryForm(request.POST or None, instance=country)
	if country_form.is_valid():
		the_country = country_form.save(commit=False)
		the_country.edited = datetime.datetime.utcnow().replace(tzinfo=utc)
		the_country.log = ModelLog.create_log(request.user, country, the_country)
		the_country.save()
			
		return HttpResponseRedirect(reverse('country'))
			
	return render(request, 'create_country.html', {'country_form': country_form, 'form_url': form_url, 'country_id': country.id})
	
	
def delete_country(request, country_id):
	## check if user is logged in
	#if not request.user.is_authenticated():
		#return HttpResponseRedirect(reverse('login_user'))
	
	#del_country = get_object_or_404(Country, pk=country_id)
	
	#if request.POST:
		#print del_country
		#del_country.delete()
		#return HttpResponseRedirect(reverse('country'))
	
	#return render(request, 'delete_country.html',{'del_country': del_country})
	pass

def province(request):
	# Check if user is logged in
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login_user'))
	
	# List all countries in table with basic information
	provinces = Province.objects.order_by('name')
	
	return render(request, 'province.html', {'provinces': provinces})

def create_province(request):
	# check if user is logged in
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login_user'))
	
	form_url = "create"
	
	if request.POST:
		province_form = ProvinceForm(request.POST)
		if province_form.is_valid():
			new_province = province_form.save(commit=False)
			new_province.edited = datetime.datetime.utcnow().replace(tzinfo=utc)
			new_province.log = ModelLog.create_log(request.user, new_province, new_province)
			province_form.save()
			return HttpResponseRedirect(reverse('province'))
			
		else:
			return render(request, 'create_province.html', {'province_form': province_form, 'form_url': form_url})
				
	province_form = ProvinceForm()
	
	return render(request, 'create_province.html', {'province_form': province_form, 'form_url': form_url})



def edit_province(request, province_id):
	# check if user is logged in
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login_user'))
		
	province = get_object_or_404(Province, pk=province_id)
	form_url = "edit"
	
	province_form = ProvinceForm(request.POST or None, instance=province)
	if province_form.is_valid():
		province = country_form.save(commit=False)
		province.edited = datetime.datetime.utcnow().replace(tzinfo=utc)
		province.log = ModelLog.create_log(request.user, country, new_country)
		province.save()
			
		return HttpResponseRedirect(reverse('province'))
			
	return render(request, 'create_province.html', {'province_form': province_form, 'form_url': form_url, 'province_id': province.id})


def delete_province(request, province_id):
	pass


def region(request):
	# check if user is logged in
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login_user'))
	
	pass	
	

def create_region(request):
	# check if user is logged in
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login_user'))
	
	pass



def edit_region(request):
	pass
