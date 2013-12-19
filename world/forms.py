from django import forms
from world.models import Country, Province, Region



class CountryForm(forms.ModelForm):
	"""Form to create or edit Countries."""
	
	name = forms.CharField()
	flavor = forms.CharField(
					widget=forms.Textarea(attrs={'width': 300, 'height': 100}))
	history = forms.CharField(
					widget=forms.Textarea(attrs={'width': 300, 'height': 100}))
	
	
	class Meta:
		model = Country
		fields = ['name', 'flavor', 'history']
		exclude = ['approved', 'edited']
		
	def clean_name(self):
		name = self.cleaned_data['name'].title()
		qs = Country.objects.filter(name=name)
	
		if self.instance.pk is not None:
			qs = qs.exclude(pk=self.instance.pk)
		if qs.exists():
			raise forms.ValidationError("There is already a country with name: %s" % name)	
		
		if Province.objects.filter(name=name).exists():
			raise forms.ValidationError(("There is already a province with the name: %s") % data)
		if Region.objects.filter(name=name).exists():
			raise forms.ValidationError(("There is already a region with the name: %s") % data) 
	
		return name

		
		
		
		
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
		exclude = ['approved', 'edited']
	
	def clean_name(self):
		name = self.cleaned_data['name'].title()
		qs = Province.objects.filter(name=name)
	
		if self.instance.pk is not None:
			qs = qs.exclude(pk=self.instance.pk)
		if qs.exists():
			raise forms.ValidationError("There is already a province with name: %s" % name)	
			
		if Country.objects.filter(name=name).exists():
			raise forms.ValidationError(("There is already a country with the name: %s") % data)
		if Region.objects.filter(name=name).exists():
			raise forms.ValidationError(("There is already a region with the name: %s") % data) 
	
		return name
	

class RegionForm(forms.ModelForm):
	"""Form to create or edit Regions."""
	
	class Meta:
		model = Region
		exclude = ['approved', 'edited']
	
	def clean_name(self):
		name = self.cleaned_data['name'].title()
		qs = Region.objects.filter(name=name)
	
		if self.instance.pk is not None:
			qs = qs.exclude(pk=self.instance.pk)
		if qs.exists():
			raise forms.ValidationError("There is already a region with name: %s" % name)	
		
		if Province.objects.filter(name=name).exists():
			raise forms.ValidationError(("There is already a province with the name: %s") % data)
		if Country.objects.filter(name=name).exists():
			raise forms.ValidationError(("There is already a country with the name: %s") % data) 
	
		return name
		
		
