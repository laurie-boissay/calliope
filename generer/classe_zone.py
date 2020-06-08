from random import randrange

from collection_de_mots.zone import *
from collection_de_mots.personnes import *

from generer.mechanismes_zones import *


class Zone:
	"""
	Tous les attributs et méthodes nécessaires pour générer une zone.
	"""

	def __init__(self):

		self.zone = {
			"superficie" : "",
			"population" : "",
			"densité" : "",
			"richesse" : "",
			"activité" : "",
			"nom" : "",
			"climat" : "",
			}

		self.activite = ""
		self.densite = ""
		self.richesse = ""
		self.superficie = ""

		self.commande = "\n\n\*\*\*  *Description complète avec cette commande :*  \*\*\*"
		self.description = ""

	
	def contraintes(self, message):

		parametres_zone = message.split(",")

		for param in range(len(parametres_zone)):
			contrainte = parametres_zone[param].split("=")
			for key in self.zone.keys():
				if contrainte[0].strip(" ") == key:
					valeur = contrainte[1].strip(" ")
					if key == "nom":
						self.zone[key] = valeur
					else:
						self.zone[key] = valeur.lower()


	def set_zone(self):
		self.zone["superficie"], self.superficie = zone_attribut_avec_indice(self.zone["superficie"], superficie)
		self.zone["densité"], self.densite = zone_attribut_avec_indice(self.zone["densité"], densite)
		self.zone["richesse"], self.richesse = zone_attribut_avec_indice(self.zone["richesse"], richesse)
		self.set_zone_pop()
		self.set_climat()
		self.set_activite()
		self.set_nom()

	
	def set_zone_pop(self):

		if self.zone["population"] == "":
			self.zone["population"] = pers_race[randrange(len(pers_race))]


	def set_climat(self):

		if self.zone["climat"] == "":
			self.zone["climat"] = climat[randrange(len(climat))]


	def set_activite(self):

		if self.zone["activité"] == "":
			self.zone["activité"] = self.activite = activite[randrange(len(activite))]

		elif self.zone["activité"] in activite:
			self.activite = self.zone["activité"]

		else:		
			mots = self.zone["activité"].split(" ")
			
			for i in range(len(mots)):
				mots[i] = mots[i].split("'")
				
				for j in range(len(mots[i])):
					
					for k in range(len(activite)):
						
						if mots[i][j] in activite[k] and len(mots[i][j]) > 5:
							self.activite = activite[k]

			if self.activite == "":
				self.activite = activite[randrange(len(activite))]


	def set_description(self):
		texte = "C'est une " + self.zone["superficie"] + " zone " + self.zone["densité"]

		if self.densite > 2 and self.superficie > 3:
			cosmopolite_ou_race.append(self.zone["population"])
			pop = cosmopolite_ou_race[randrange(len(cosmopolite_ou_race))]
			cosmopolite_ou_race.remove(self.zone["population"])

			if pop == "cosmopolite":
				texte += " et cosmopolite"
			else:
				texte += " habitée majoritairement par des " + self.zone["population"]

		else:
			texte += " habitée majoritairement par des " + self.zone["population"]

		texte += ".\n" + "L'activité principale est " + self.zone["activité"] + ". "
		texte += "La population est " + self.zone["richesse"] + ". Le climat est "
		texte += self.zone["climat"] + ". La zone est " + paysage[randrange(len(paysage))] + "."


		texte += "\n\n*Comment personnaliser cette zone :*"
		texte += "```!description```"

		self.description += texte

		return self.description


	def set_nom(self):
		if self.zone["nom"] == "":
			self.zone["nom"] = nom_zone(self.zone["superficie"], self.zone["richesse"],self.zone["densité"], self.zone["activité"])


	def set_commande(self):
		texte = "\n\n> *!zone"

		self.zone["superficie"] = str(self.superficie)
		self.zone["densité"] = str(self.densite) 
		self.zone["richesse"] = str(self.richesse)

		for key, value in self.zone.items():
			texte += ", " + key + "=" + value

		texte += "*"
		self.commande += texte


	def get_zone_nom(self):
		return self.zone["nom"]


	def get_commande(self):
		return self.commande