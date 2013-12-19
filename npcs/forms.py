from django import forms
from npcs.models import Faction, NPCGuild


class FactionForm(forms.ModelForm):
	"""Form to create or edit Countries."""
	
	name = forms.CharField()
	flavor = forms.CharField(
					widget=forms.Textarea(attrs={'width': 300, 'height': 100}))
	history = forms.CharField(
					widget=forms.Textarea(attrs={'width': 300, 'height': 100}))
	likes_set = Faction.objects.all()
	likes = forms.ModelChoiceField(queryset=likes_set, empty_label="Country it likes", required=False)
	hates_set = Faction.objects.all()
	hates = forms.ModelChoiceField(queryset=hates_set, empty_label="Country it hates", required=False)
	
	
	#def __init__(self, *args, **kwargs):
		#super(FactionForm, self).__init__(*args, **kwargs)
		#if 'instance' in kwargs:
			#self.fields['likes'].queryset = Faction.objects.exclude(kwargs['instance'])
			#self.fields['hates'].queryset = Faction.objects.exclude(kwargs['instance'])
	
	
	class Meta:
		model = Faction
		fields = ['name', 'likes', 'hates', 'flavor', 'history']
		exclude = ['approved', 'edited']
	
		
	def clean_name(self):
		name = self.cleaned_data['name'].title()
		qs = Faction.objects.filter(name=name)
	
		if self.instance.pk is not None:
			qs = qs.exclude(pk=self.instance.pk)
		if qs.exists():
			raise forms.ValidationError("There is already a faction with name: %s" % name)	
		if NPCGuild.objects.filter(name=name).exists():
			raise forms.ValidationError(("There is already a NPC guild with the name: %s") % data)
		return name
	
	# check if likes is not the same as hates
	def clean(self):
		cleaned_data = super(FactionForm, self).clean()
		likes = cleaned_data.get("likes")
		hates = cleaned_data.get("hates")
		n_objects = Faction.objects.all().count()
		
		if n_objects == 0:
			pass
		elif likes == hates:
			print likes, hates
			raise forms.ValidationError("Your friend cannot be your enemy aswell")
		
		return cleaned_data


# form for managing NPC Guild edit/creation
class NPCGuildForm(forms.ModelForm):
	"""Form to create or edit NPC Guilds"""
	
	name = forms.CharField()
	category = forms.ChoiceField(choices=NPCGuild.CATEGORIES)
	faction_set = Faction.objects.all()
	faction = forms.ModelChoiceField(queryset=faction_set, empty_label="Faction", required=True)
	
	
	class Meta:
		model = NPCGuild
		fields = ['name', 'category', 'faction', 'flavor']
		exclude = ['approved', 'edited']
	
	
	# Check if name is unique
	def clean_name(self):
		name = self.cleaned_data['name'].title()
		qs = NPCGuild.objects.filter(name=name)
	
		if self.instance.pk is not None:
			qs = qs.exclude(pk=self.instance.pk)
		if qs.exists():
			raise forms.ValidationError("There is already a NPC Guild with name: %s" % name)	
		if Faction.objects.filter(name=name).exists():
			raise forms.ValidationError(("There is already a Faction with the name: %s") % data)
		return name
