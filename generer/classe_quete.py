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

		self.contexte_de_quete = ""


	def set_mission_commanditaire(self, cmd_text):
		"""
		Prend en entrée le texte de la commande.

		Regarde si le type quête est définit par
		l'utilisateur.

		Enregistre le type de quête.
		"""
		parametres = cmd_text.split(",")

		if parametres[1].strip(" ") in quete:
			self.type_quete = parametres[1].strip(" ")


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
			self.recompense += "\n*!pj, 12, 3, prénom=" + self.pnj_commanditaire['prénom'] + ", nom="
			self.recompense += self.pnj_commanditaire['nom'] + ", métier=" + self.pnj_commanditaire['métier']
			self.recompense += ", race=" + self.pnj_commanditaire['race'] + ", genre="
			self.recompense += self.pnj_commanditaire["genre"] + ", secret=" + self.pnj_commanditaire["secret"]
			self.recompense += ", age=" + self.pnj_commanditaire["age"] + "*"

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

		elif self.type_commanditaire == "un réseau":
			metier = poste_guilde[randrange(len(poste_guilde))] + " d'un réseau " + self.commanditaire


		perso.set_metier(metier)
		perso.set_particularites()
		return perso.pnj_light()


	def gen_pnj_light(self, type_metier, lieu_metier) :

		perso = Personnage()

		metier = ""
		if type_metier == "une organisation":
			if lieu_metier == "le palais de justice":
				metier = poste_palais_justice[randrange(len(poste_palais_justice))] + " au palais de justice"
			elif lieu_metier == "la caserne":
				metier = poste_caserne[randrange(len(poste_caserne))] + " dans la caserne"
			elif lieu_metier == "La capitainerie":
				metier = poste_capitainerie[randrange(len(poste_capitainerie))] + " dans la capitainerie"
			elif lieu_metier == "le chateau":
				metier = poste_chateau[randrange(len(poste_chateau))] + " dans le chateau"
			elif lieu_metier == "le temple":
				metier = poste_temple[randrange(len(poste_temple))] + " dans le temple"
			else : # la guilde des voleurs, marchands, assassins, prostituées, médecins
				metier = poste_guilde[randrange(len(poste_guilde))] + " de " + lieu_metier

		elif type_metier == "un réseau":
			metier = poste_guilde[randrange(len(poste_guilde))] + " d'un réseau " + lieu_metier


		perso.set_metier(metier)
		perso.set_particularites()
		return perso.pnj_light()

	def assembler_texte_de_quete(self):
		texte_de_quete = self.contexte_de_quete

		text = [
		# Déscription du pnj commanditaire :
		"Les héros rencontrent ", self.description_personne(self.pnj_commanditaire), "\n",

		self.pnj_commanditaire["prénom"]," leur demande ", 

		# Description de la quête :
		self.quete,

		# Aide reçue :
		"\n", self.aide,

		# Récompense promise :
		"\n\n", self.pnj_commanditaire["prénom"], " propose de récompenser les héros ", 
		self.recompense,
		]

		for i in range(len(text)):
			texte_de_quete += text[i]

		return texte_de_quete

#___________Méchanismes_de_quête________________________________________________

	def generer_quete(self):
		"""
		Décide du type de quête :
		voler, infiltrer, protéger, livrer, enquêter, kidnaper, tuer, détruire,
		trouver, sauver, fabriquer, capturer, empoisonner et intercepter.
		"""

		if self.type_quete == "voler" :
			self.quete += "de __**voler**__ " + self.truc_a_voler() + self.qui_paye()

		elif self.type_quete == "infiltrer" :
			self.quete += "d'__**infiltrer**__ " + mission_infiltrer()
		
		elif self.type_quete == "protéger" :
			self.quete += "de __**protéger**__ " + cible_protection()
		
		elif self.type_quete == "livrer" :
			self.quete += "de __**livrer**__ " + cible_livraison() + self.qui_paye()
		
		elif self.type_quete == "enquêter" :
			self.quete += "d'__**enquêter**__ sur " + self.mission_enqueter()
		
		elif self.type_quete == "kidnaper" :
			self.quete += "de __**kidnaper**__ " + mission_kidnaper() + "\n" + self.qui_paye()

		elif self.type_quete == "tuer" :
			self.quete += "de __**tuer**__ " + mission_tuer()

		elif self.type_quete == "détruire" :
			self.quete += "de __**détruire**__ " + mission_detruire()

		elif self.type_quete == "trouver" :
			self.quete += "de __**trouver**__ "+ objet_precieux() + " dans " + lieu_quete()
			self.quete += "." + ou_nature()

		elif self.type_quete == "sauver" :
			personne = self.generer_pnj_light()
			self.set_commanditaire()
			self.quete += "de __**sauver**__ " + self.description_personne(personne)
			self.quete += "\nLes héros trouverons cette personne dans "
			self.quete += type_lieu_ville() + menace("une personne")

		elif self.type_quete == "fabriquer" :
			self.quete += "de __**fabriquer**__ " + self.mission_fabriquer()

		elif self.type_quete == "capturer" :
			self.quete += "de __**capturer**__ " + animal_sacre() + " dans " + lieu_quete_ext()
			self.quete += "." + ou_nature() + "\n" + self.qui_paye()

		elif self.type_quete == "empoisonner" :
			self.quete += "de __**empoisonner**__ " + mission_empoisonement()

		elif self.type_quete == "intercepter" :
			self.quete += "de __**intercepter**__ " + mission_intercepter()

	
	def coupable(self, coupable):
		text = ""
		text += coupable["prénom"] + " " + coupable["nom"] + ". " + coupable["pronom"]  
		text += " est " + coupable["métier"] + ".\n" + coupable["prénom"] + " est de la race des "
		text += coupable["race"] + "s" + ". C'est une personne " + coupable["age"]
		text += ", de genre " + coupable["genre"] + "."
		text += "\n\n*!pnj, 12, 3, prénom=" + coupable['prénom'] + ", nom=" + coupable['nom']
		text += ", métier=" + coupable['métier'] + ", race=" + coupable['race'] 
		text += ", genre=" + coupable["genre"] + ", age=" + coupable["age"] + "*" + ".\n"
		return text
	

	def victime_morte(self, victime):
		text = ""
		text += "La victime était une personne " + victime["age"] + " de genre " + victime["genre"]
		text += ".\n" + victime["pronom"] + " s'appelait " + victime["prénom"] + " " + victime["nom"]
		text += ". " + victime["pronom"] + " était de la race des " + victime["race"] + "s.\n"
		text += victime["pronom"] + " exerçait le métier de " + victime["métier"] + ". "
		text += victime["prénom"] + " cachait un secret " + victime["secret"] + ".\n"
		return text


	def description_personne(self, personne):
		text = ""
		
		text += personne["prénom"] + " " + personne["nom"] + ". C'est une personne "
		text += personne["age"] + " de genre " + personne["genre"] 
		text += ", de la race des " + personne["race"] + "s.\n"
		text += personne["pronom"] + " est " + personne["métier"] + ". "
		text += personne["prénom"] + " cache un secret " + personne["secret"] + "."
		text += "\n\n*!pnj, 12, 3, prénom=" + personne['prénom'] + ", nom=" + personne['nom']
		text += ", métier=" + personne['métier'] + ", race=" + personne['race'] 
		text += ", genre=" + personne["genre"] + ", secret=" + personne["secret"]
		text += ", age=" + personne["age"] + "*" + "\n"
		return text
		

	def mission_enqueter(self):
		"""
		Le propos de l'enquête :
		un meurtre, un kidnaping, une organisation, un réseau, une personne, un vol.
		"""
		coupable = self.generer_pnj_light()
		self.set_commanditaire()
		victime = self.generer_pnj_light()

		raison = enquete[randrange(len(enquete))]

		text = ""

		if raison == "un meurtre" :
			self.type_commanditaire = "une organisation"
			self.commanditaire = commanditaires_enqueter_meurtre[randrange(len(commanditaires_enqueter_meurtre))]

			if self.commanditaire == "le chateau" or self.commanditaire == "le temple":
				victime = self.generer_pnj_light()
				self.contexte_de_quete += "Un messager arrive à l'auberge où logent les héros."
				self.contexte_de_quete += " Il leur annonce qu'ils sont attendus dans "
				self.contexte_de_quete += self.commanditaire + ". C'est une mission très confidentielle :\n\n"

			text += "un meurtre : \n\n"
			text += self.victime_morte(victime)
			text += "\nLe corps a été retrouvé " + scene_crime() + " "
			text += description[randrange(len(description))] + ".\n"
			text += "Le mobile est " + mobile[randrange(len(mobile))] + "."
			text += "\n\nLe coupable est " + self.coupable(coupable)
		
		elif raison == "un kidnaping" :
			text += "un kidnaping : \n\n"
			text += self.enquete_kidnaping()
		
		elif raison == "une organisation" :
			self.type_commanditaire = "une organisation"
			self.commanditaire = organisation[randrange(len(organisation))]
			coupable = self.generer_pnj_light()
			text += self.commanditaire +" :\n\nLes héros doivent démasquer un espion.\nC'est "
			text += self.coupable(coupable)
			
		elif raison == "une personne" :
			text += "une personne :\n\nIl s'agit de " + self.description_personne(coupable)
		
		elif raison == "un vol" :
			text += "un vol :\n\nIl s'agit de " + truc_a_voler() + "\n\nLe coupable est "
			text += self.coupable(coupable)
		
		else : #"un réseau"
			nom_reseau = reseau[randrange(len(reseau))]
			text += "un réseau " + nom_reseau + "\n\nLes héros doivent démasquer le chef de ce réseau.\nC'est "
			text += self.coupable(coupable)

		return text


	def enquete_kidnaping(self) :
		"""
		Détails pour résoudre l'enquête du kidnaping.
		- qui a été enlevé ;
		- ou cette personne est-elle retenue ;
		- qui est le coupable ;
		- quel est le mobile.
		"""

		coupable = self.generer_pnj_light()
		self.set_commanditaire()
		victime = self.generer_pnj_light()

		text = "Il s'agit de " + self.description_personne(victime) + "\n"
		text += victime["pronom"] + " est retenu.e "
		scene = lieu_crime[randrange(len(lieu_crime))]

		if scene == "lieu discret" :
			text += lieu_discret[randrange(len(lieu_discret))] + "."
			text += "\n\nLe coupable est " + self.coupable(coupable)

		elif scene == "une maison" :
			text += maison[randrange(len(maison))] + "."
			text += "\n\nLe coupable est " + self.coupable(coupable)
		else : # "une organisation" :
			nom_organisation = organisation[randrange(len(organisation))]
			text += "dans " + nom_organisation + "."
			coupable = self.gen_pnj_light("une organisation", nom_organisation)
			text += "\n\nLe coupable est " + self.coupable(coupable)
		
		text += "\nLe mobile est " + mobile[randrange(len(mobile))] + "."
		
		return text


	def qui_paye(self) :
		"""
		Définit un point de livraison.
		une organisation, un lieu discret, la maison de quelqu'un, une auberge.
		"""
		type_payeur = self.type_commanditaire
		payeur = self.commanditaire

		if type_payeur == "une organisation" :
			text = "\nLa livraison se fera dans " + payeur + ". Ils seront attendus."

		elif type_payeur == "un réseau" :
			contact = lieu_discret[randrange(len(lieu_discret))]
			text = "\nLa livraison est pour le réseau " + payeur
			text += ". Ils trouverons leur contact " + contact

			if contact == "dans la taverne" :
				text += " : " + nom_auberge() + "."
			else :
				text += "."
		else :
			personne = self.generer_pnj_light()
			text = "\nLa livraison se fera chez " + self.description_personne(self, personne)

		return text


	def truc_a_voler(self) :
		"""
		Définit un nombre d'objets ou d'animaux et génère des détails sur l'endroit ou les trouver
		et la personne à qui ils appartiennent.
		"""
		personne = self.generer_pnj_light()
		self.set_commanditaire()

		truc = vol[randrange(len(vol))]

		if truc == "objet personnel" :
			text = objet_pers[randrange(len(objet_pers))] + ". Chez "
			text += self.description_personne(personne)
		
		elif truc == "caisse" :
			text = str(randrange(1 , 10, 1)) + " caisse(s) " + caisse[randrange(len(caisse))]
			text += " dans "+ type_lieu_ville()

		return text


	def mission_fabriquer(self) :
		"""
		Définit les 3 étapes nécessaires pour résoudre une quête de type "fabriquer":
			- ou trouver les composants ;
			- ou fabriquer l'objet ;
			- quel monstre tuer avec cet objet et ou le trouver.
		"""
		self.type_commanditaire = "une organisation"
		self.commanditaire = "le temple"

		text = objet_precieux() + " :\n"
		
		text += "\n1) Il leur faudra d'abord trouver les composants dans " 
		text += lieu_quete()+ "." + ou_nature()
		
		text += "\n\n2) Puis ils se rendront dans " + lieu_quete()
		text += " pour fabriquer l'objet." + ou_nature()

		text += "\n\n3) Leur quête prendra fin lorsqu'ils aurront terrassé "
		text += quel_monstre() + " dans "+ lieu_quete_ext() + "." + ou_nature()
	
		return text