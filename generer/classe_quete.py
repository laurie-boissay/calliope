from random import randrange

from generer.mechanismes_quete import *

from generer.quete import *

from collection_de_mots.quetes import *

from generer.classe_personnage import Personnage


class Quete:
	

	def __init__(self):

		self.type_quete = ""
		self.quete = ""

		self.type_commanditaire = ""
		self.commanditaire = ""
		self.pnj_commanditaire = {}

		self.aide = ""
		self.pnj_aide = {}

		self.type_recompense = ""
		self.recompense = ""


	def set_mission_commanditaire(self, cmd_text):
		"""
		Prend en entrée le texte de la commande.

		Regarde si la mission et le commanditaire sont définit par
		l'utilisateur.

		Enregistre les valeurs définits.
		"""
		parametres = cmd_text.split(",")

		for i in range(1, len(parametres)):
			couple = parametres[i].split("=")

			if couple[0].strip(" ") == "mission":
				self.type_quete = couple[1].strip(" ")


		#print("type_quete : ", self.type_quete, "\n")
	

	def combler_les_manques(self):
		"""
		Assigne des valeurs aux attributs vides.
		"""
		if self.type_commanditaire == "":
			self.type_commanditaire = commanditaire[randrange(len(commanditaire))]

		if self.commanditaire == "":
			self.set_commanditaire()

		if self.type_quete == "":
			self.type_quete = quete[randrange(len(quete))]

		if self.quete == "":
			self.generer_quete()

		if self.pnj_commanditaire == {}:
			self.pnj_commanditaire = self.generer_pnj_light()

		if self.aide == "":
			self.set_aide()

		if self.recompense == "":
			self.set_recompense()

		

		#print("type_quete : ", self.type_quete, "\n")
		#print("quete : ", self.quete, "\n\n")

		#print("type_commanditaire : ", self.type_commanditaire, "\n")
		#print("commanditaire : ", self.commanditaire)
		#print("pnj_commanditaire : ", self.pnj_commanditaire, "\n\n")

		#print("aide : ", self.aide, "\n\n")

		#print("type_recompense : ", self.type_recompense, "\n")
		#print("recompense : ", self.recompense, "\n")



	def set_commanditaire(self) :
		"""
		Qui engage les héros ?
		"""

		if self.type_commanditaire == "une organisation" :
			self.commanditaire = organisation[randrange(len(organisation))]

		elif self.type_commanditaire == "un réseau" :
			self.commanditaire = reseau[randrange(len(reseau))]
			
		else :
			self.commanditaire = "une personne"


	def set_aide(self):
		"""
		Définit quelle genre d'aide les PNJ recevront.
		"""

		aide = adjuvant[randrange(len(adjuvant))]
	
		if aide == "personne" :
			self.pnj_aide =  self.generer_pnj_light()
			#print("PNJ aide", self.pnj_aide)
			
			aide = [
			"Les héros auront l'appui de ", self.pnj_aide["prénom"], 
			" ", self.pnj_aide["nom"], ".\n",
			"C'est une personne ", self.pnj_aide["age"],
			", de genre ", self.pnj_aide["genre"],
			", de la race des ", self.pnj_aide["race"], "s.\n",
			self.pnj_aide["pronom"], " est ", self.pnj_aide["métier"], "."
			]

			self.aide = ""
			for i in range(len(aide)):
				self.aide += aide[i]

		elif aide == "non" :
			self.aide =  "Les héros devront se débrouiller seuls."
		else : #"matériel"
			self.aide =  "Les héros se voient proposer une aide matérielle."

	def set_recompense(self):

		metier = self.pnj_commanditaire["métier"].split(" ")
		
		if self.pnj_aide != {}:
			metier_2 = self.pnj_aide["métier"].split(" ")

			if metier_2[0] == "reine/roi" or metier_2[0] == "ministre" or metier_2[0] == "conseiller/e":
				self.recompense = "avec un titre et des terres."
				print("PNj aide", self.pnj_aide["métier"])

		if metier[0] == "reine/roi" or metier[0] == "ministre" or metier[0] == "conseiller/e":
			self.recompense = "avec un titre et des terres."

		elif metier[0] == "servante/serviteur":
			lieu = list(self.pnj_commanditaire["métier"].split("dans "))
			self.recompense = "avec une autorisation d'accès officieuse dans " + lieu[1] + "."

		elif metier[0] == "haut-placé/e":
			lieu = list(self.pnj_commanditaire["métier"].split("dans "))
			self.recompense = "en les recrutant dans " + lieu[1] + "."

		elif metier[0] == "marchand/e":
			marchandises = list(self.pnj_commanditaire["métier"].split("dans "))
			self.recompense = "avec quelques " + marchandises[1] + " de sa boutique."

		elif self.commanditaire == "la caserne":
			self.recompense = "avec un entraînement à manier l'arme de leur choix."

		elif metier[0] == "capitaine":
			self.recompense = "avec quelques " + commerce[randrange(len(commerce))] + " de sa cargaison."

		elif metier[0] == "artisan/ne" or metier[0] == "astrologue" or metier[0] == "alchimiste":
			self.recompense = "en mettant ses talents d'" + self.pnj_commanditaire["métier"] + " à leur service."

		elif metier[0] == "forgeron/ne" or metier[0] == "cartographe" or metier[0] == "sorcier/sorcière":
			self.recompense = "en mettant ses talents de " + self.pnj_commanditaire["métier"] + " à leur service."

		elif metier[0] == "apprenti/e" or metier[0] == "mendiant/e":
			self.recompense = "en se mettant à leur service."

		elif metier[0] == "tavernier/e":
			auberge = list(self.pnj_commanditaire["métier"].split("dans "))
			self.recompense = "en leur offrant un tarif préféreciel dans " + auberge[1] + "."

		elif metier[0] == "médecin" or self.commanditaire == "la guilde des médecins":
			self.recompense = "en leur offrant un tarif préféreciel sur tous les soins."

		elif self.commanditaire == "la guilde des marchands":
			self.recompense = "en leur offrant un tarif préféreciel dans toutes les boutiques de la ville."

		elif self.commanditaire == "la guilde des prostituées":
			self.recompense = "en leur offrant un tarif préféreciel dans toutes les maisons closes de la ville."

		elif metier[0] == "prêtre/sse" or self.commanditaire == "le temple":
			self.recompense = "avec un objet très précieux, sûrement magique : " + objet_precieux() + "."

		elif self.commanditaire == "la guilde des voleurs" or self.commanditaire == "la guilde des assassins":
			self.recompense = "en leur garantissant la protection de la guilde."

		else:
			self.recompense = "avec " + recompense_de_quete[randrange(len(recompense_de_quete))] + "."

		print("commanditaire : ", self.commanditaire)
		print(self.pnj_commanditaire["métier"])
		print(self.recompense, "\n")

		
	def generer_pnj_light(self) :

		perso = Personnage()

		metier = ""			
		if self.type_commanditaire == "une organisation":
			if self.commanditaire == "le palais de justice":
				metier = poste_palais_justice[randrange(len(poste_palais_justice))] + " au palais de justice"
			elif self.commanditaire == "la caserne":
				metier = poste_caserne[randrange(len(poste_caserne))] + " dans la caserne"
			elif self.commanditaire == "La capitainerie":
				metier = poste_capitainerie[randrange(len(poste_capitainerie))] + " dans la capitainerie"
			elif self.commanditaire == "le chateau":
				metier = poste_chateau[randrange(len(poste_chateau))] + " dans le chateau"
			elif self.commanditaire == "le temple":
				metier = poste_temple[randrange(len(poste_temple))] + " dans le temple"
			else : # la guilde des voleurs, marchands, assassins, prostituées, médecins
				metier = poste_guilde[randrange(len(poste_guilde))] + " de " + self.commanditaire

		if self.type_commanditaire == "un réseau":
			metier = poste_guilde[randrange(len(poste_guilde))] + " d'un réseau " + self.commanditaire


		perso.set_metier(metier)
		perso.set_particularites()
		return perso.pnj_light()


	def assembler_texte_de_quete(self):
		texte_de_quete = ""

		text = [
		# Déscription du pnj commanditaire :
		"Les héros rencontrent ", self.pnj_commanditaire["prénom"], " ", self.pnj_commanditaire["nom"], 
		". C'est une personne ", self.pnj_commanditaire["age"], ", de genre ",
		self.pnj_commanditaire["genre"], ", de la race des ", self.pnj_commanditaire["race"],"s.\n",
		self.pnj_commanditaire["pronom"], " est ", self.pnj_commanditaire["métier"], ". ",
		self.pnj_commanditaire["pronom"], " cache un secret ", self.pnj_commanditaire["secret"],
		".\n\n", self.pnj_commanditaire["prénom"]," leur demande ", 

		# Description de la quête :
		self.quete,

		# Aide reçue :
		"\n\n", self.aide,

		# Récompense promise :
		"\n\n", self.pnj_commanditaire["prénom"], " propose de récompenser les héros ", 
		self.recompense,
		]

		for i in range(len(text)):
			texte_de_quete += text[i]

		return texte_de_quete


	def generer_quete(self):
		"""
		Décide du type de quête :
		voler, infiltrer, protéger, livrer, enquêter, kidnaper, tuer, détruire,
		trouver, sauver, fabriquer, capturer, empoisonner et intercepter.
		"""

		if self.type_quete == "voler" :
			self.quete += "de __**voler**__ " + truc_a_voler()+qui_paye()

		elif self.type_quete == "infiltrer" :
			self.quete += "d'__**infiltrer**__ " + mission_infiltrer()
		
		elif self.type_quete == "protéger" :
			self.quete += "de __**protéger**__ " + cible_protection()
		
		elif self.type_quete == "livrer" :
			self.quete += "de __**livrer**__ " + cible_livraison()+qui_paye()
		
		elif self.type_quete == "enquêter" :
			self.quete += "d'__**enquêter**__ sur " + self.mission_enqueter()
		
		elif self.type_quete == "kidnaper" :
			self.quete += "de __**kidnaper**__ " + mission_kidnaper() + "\n" + qui_paye()

		elif self.type_quete == "tuer" :
			self.quete += "de __**tuer**__ " + mission_tuer()

		elif self.type_quete == "détruire" :
			self.quete += "de __**détruire**__ " + mission_detruire()

		elif self.type_quete == "trouver" :
			self.quete += "de __**trouver**__ "+objet_precieux()+" dans "+lieu_quete()+"." +ou_nature()

		elif self.type_quete == "sauver" :
			self.quete += "de __**sauver**__ "+ personne()+"\nLes héros trouverons cette personne dans "+type_lieu_ville() + menace("une personne")

		elif self.type_quete == "fabriquer" :
			self.quete += "de __**fabriquer**__ " + mission_fabriquer()

		elif self.type_quete == "capturer" :
			self.quete += "de __**capturer**__ " + animal_sacre() +" dans "+ lieu_quete_ext()+ "." + ou_nature() + "\n" + qui_paye()

		elif self.type_quete == "empoisonner" :
			self.quete += "de __**empoisonner**__ " + mission_empoisonement()

		elif self.type_quete == "intercepter" :
			self.quete += "de __**intercepter**__ " + mission_intercepter()
		

	def mission_enqueter(self):
		"""
		Le propos de l'enquête :
		un meurtre, un kidnaping, une organisation, un réseau, une personne, un vol.
		"""
		victime = self.generer_pnj_light()
		coupable = self.generer_pnj_light()

		raison = enquete[randrange(len(enquete))]

		text = ""

		if raison == "un meurtre" :
			self.type_commanditaire = "une organisation"
			self.commanditaire = "la caserne"
			text += "un meurtre : \n\n"
			text += "La victime est une personne de genre " + victime["genre"] + ".\n"
			text += victime["pronom"] + " s'appelait " + victime["prénom"] + " " + victime["nom"] + "." 
			text += victime["pronom"] + " était de la race des " + victime["race"] + "s.\n"
			text += victime["pronom"] + " exerçait le métier de " + victime["métier"] + ". "
			text += victime["prénom"] + " cachait un secret " + victime["secret"] + ".\n\n"
			text += "\nLe mobile est " + mobile[randrange(len(mobile))] + ".\n"
			text += description[randrange(len(description))] + ".\n\n"
			text += "Le corps a été retrouvé " + scene_crime() + "\n\nLe coupable est " + personne()	
		
		elif raison == "un kidnaping" :
			text += "un kidnaping : \n\n"
			text += enquete_kidnaping() # cette personne est retenue : lieu en arapport avec coupable
		
		elif raison == "une organisation" :
			self.type_commanditaire = "une organisation"
			self.commanditaire = organisation[randrange(len(organisation))]
			coupable = self.generer_pnj_light()
			text += self.commanditaire +" :\n\nLes héros doivent démasquer un espion.\nC'est "
			text += coupable["prénom"] + " " + coupable["nom"] + ". " + coupable["pronom"]  
			text += " est " + coupable["métier"] + ".\n" + coupable["prénom"] + " est de la race des "
			text += coupable["race"] + ". C'est une personne " + coupable["age"] + "."
		
		elif raison == "une personne" :
			self.type_commanditaire = "une organisation"
			self.commanditaire = "le chateau"
			text += "une personne :\n\nIl s'agit de "+personne()
		
		elif raison == "un vol" :
			self.type_commanditaire = "une organisation"
			self.commanditaire = "la caserne"
			text += "un vol :\n\nIl s'agit de "+ truc_a_voler() +"\n\nLe coupable est "
			text += coupable["prénom"] + " " + coupable["nom"] + ". " + coupable["pronom"]  
			text += " est " + coupable["métier"] + ".\n" + coupable["prénom"] + " est de la race des "
			text += coupable["race"] + ". C'est une personne " + coupable["age"] + "."
		
		else : #"un réseau"
			self.type_commanditaire = "un réseau"
			self.commanditaire = reseau[randrange(len(reseau))]
			coupable = self.generer_pnj_light()
			text += "le réseau " + self.commanditaire + " :\n\nLes héros doivent démasquer un espion.\nC'est "
			text += coupable["prénom"] + " " + coupable["nom"] + ". " + coupable["pronom"]  
			text += " est " + coupable["métier"] + ".\n" + coupable["prénom"] + " est de la race des "
			text += coupable["race"] + ". C'est une personne " + coupable["age"] + "."
		
		
		return text