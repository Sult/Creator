from django.db import models


#Factions
class Faction(models.Model):
	"""
	Main factions in Buahto, chatacters choose one of these at start
	"""

	name =  models.CharField(max_length=63, unique=True)
	flavor = models.TextField()
	history = models.TextField()
	likes = models.ForeignKey(
				'self', 
				related_name='likes_faction', 
				null=True, 
				blank=True,
				on_delete=models.SET_NULL
				)
	
	hates = models.ForeignKey(
				'self', 
				related_name='hates_faction', 
				null=True, 
				blank=True,
				on_delete=models.SET_NULL
				)
	
	approved = models.BooleanField()
	edited = models.DateTimeField()
	
	@staticmethod
	def need_attention(obj):
		"""
		checkes what objects are not ready to be approved yet
		They have missing fields or other points that need attention
		"""
		
		if obj.likes == None or obj.hates == None:
			lists = [obj]
			message = []
			if obj.likes == None:
				message.append("faction should like some other country.")
			if obj.hates == None:
				message.append("country should hate some other country.")
			lists.append(message)
			return lists
	
	
	def __unicode__(self):
		return self.name



class NPCGuild(models.Model):
	"""
	NPC guidl that are linked to a faction 
	"""
	
	CATEGORIES=(
		('COM', 'Combat'),
		('CRA', 'Crafting'),
		('DIS', 'Distribution'),
		('GAT', 'Gathering'),
		('WAR', 'Warfare'),
	)
	
	
	faction = models.ForeignKey(Faction)
	category = models.CharField(max_length=3, choices=CATEGORIES)
	
	name = models.CharField(max_length=63)
	flavor = models.TextField()
	approved = models.BooleanField()
	edited = models.DateTimeField()
	
	@staticmethod
	def need_attention(obj):
		"""
		checkes what objects are not ready to be approved yet
		They have missing fields or other points that need attention
		"""

		if obj.faction == None:
			message = [obj]
			message.append("NPC Guild should be linked to a faction")
			return message
	
	def __unicode__(self):
		return self.name
