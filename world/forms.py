from django import forms
from world.models import Country, Province, Region

from methods import creator_logic

class CountryForm(forms.ModelForm):
	"""Form to create or edit Countries."""
	
	name = forms.CharField()
	flavor = forms.CharField(
					widget=forms.Textarea(attrs={'width': 300, 'height': 100}))
	history = forms.CharField(
					widget=forms.Textarea(attrs={'width': 300, 'height': 100}))
	likes_set = Country.objects.all()
	likes = forms.ModelChoiceField(queryset=likes_set, empty_label="Country it likes", required=False)
	hates_set = Country.objects.all()
	hates = forms.ModelChoiceField(queryset=hates_set, empty_label="Country it hates", required=False)
	
	
	class Meta:
		model = Country
		exclude = ['approved', 'log', 'edited']
		
	#def __init__(self, *args, **kwargs):
		#instance = kwargs.pop('instance', None)
		#super(CountryForm, self).__init__(*args, **kwargs)
		#if 'instance' in kwargs:
			#self.fields['likes'].queryset = Country.objects.exclude(kwargs['instance'])
			#self.fields['hates'].queryset = Country.objects.exclude(kwargs['instance'])
	
	def clean_name(self):
		raw_data = self.cleaned_data['name']
		data = raw_data.title()
		
		#if not (form.instance and form.instance.pk):
		if Country.objects.filter(name=data).exists():
			raise forms.ValidationError(("There is already a country with the name: %s") % data)
		if Province.objects.filter(name=data).exists():
			raise forms.ValidationError(("There is already a province with the name: %s") % data)
		if Region.objects.filter(name=data).exists():
			raise forms.ValidationError(("There is already a region with the name: %s") % data) 
		return data
	
	def clean(self):
		cleaned_data = super(CountryForm, self).clean()
		likes = cleaned_data.get("likes")
		hates = cleaned_data.get("hates")
		
		if likes == hates:
			raise forms.ValidationError("Your friend cannot be your enemy aswell")
		
		return cleaned_data
		
		
		
		
class ProvinceForm(forms.ModelForm):
	"""Form to create or edit Provinces."""
	
	name = forms.CharField()
	choice_set = Country.objects.all()
	country = forms.ModelChoiceField(queryset=choice_set, empty_label="Choose its country")
	flavor = forms.CharField(
						widget=forms.Textarea(attrs={'width': 300, 'height': 200}))
	history = forms.CharField(
						widget=forms.Textarea(attrs={'width': 300, 'height': 200}))
	
	class Meta:
		model = Province
		fields = ['name', 'country', 'flavor', 'history']
		exclude = ['approved', 'log', 'edited']
	
	def clean_name(self):
		raw_data = self.cleaned_data['name']
		data = raw_data.title()
		
		#if not (form.instance and form.instance.pk):
		if Country.objects.filter(name=data).exists():
			raise forms.ValidationError(("There is already a country with the name: %s") % data)
		if Province.objects.filter(name=data).exists():
			raise forms.ValidationError(("There is already a province with the name: %s") % data)
		if Region.objects.filter(name=data).exists():
			raise forms.ValidationError(("There is already a region with the name: %s") % data) 
		return data
	

class RegionForm(forms.ModelForm):
	"""Form to create or edit Regions."""
	
	class Meta:
		model = Region
		exclude = ['approved', 'log', 'edited']
	
	def clean_name(self):
		raw_data = self.cleaned_data['name']
		data = raw_data.title()
		
		#if not (form.instance and form.instance.pk):
		if Country.objects.filter(name=data).exists():
			raise forms.ValidationError(("There is already a country with the name: %s") % data)
		if Province.objects.filter(name=data).exists():
			raise forms.ValidationError(("There is already a province with the name: %s") % data)
		if Region.objects.filter(name=data).exists():
			raise forms.ValidationError(("There is already a region with the name: %s") % data) 
		return data
		
		
