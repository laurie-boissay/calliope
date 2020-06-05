from random import randrange

from generer.mechanismes_quete import *
from generer.classe_personnage import Personnage
from generer.quete import *

from collection_de_mots.quetes import *


class Quete:
	"""
	Tous les attributs et méthodes nécessaires pour générer une quête.
	"""

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
		self.presentation_commanditaire = ""


	def set_mission_commanditaire(self, cmd_text):
		"""
		Prend en entrée le texte de la commande.

		Regarde si le type quête est définit par
		l'utilisateur.

		Enregistre le type de quête.
		"""
		parametres = cmd_text.split("=")


		if len(parametres) == 2  and parametres[1].strip(" ") in quete:
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


	def exclure_type_commanditaire(self, quel_type_commanditaires):
		"""
		Prends un type de commanditaire en entrée.

		Tant que self.type_commanditaire correspond, la fonction
		génère un nouveau commanditaire et assigne sa valeur à
		self.type_commanditaire
		"""
		while self.type_commanditaire == quel_type_commanditaires:
			self.type_commanditaire = commanditaire[randrange(len(commanditaire))]
			self.set_commanditaire()


	def nomer_commanditaire(self):
		"""
		Permet de parler du commanditaire sans utiliser le 
		mot commanditaire.

		Renvoie un mot plus précis.
		"""
		if self.type_commanditaire == "une organisation":
			text = self.commanditaire.capitalize()

		elif self.type_commanditaire == "un réseau":
			text = "Le réseau " + self.commanditaire

		else:
			text = self.pnj_commanditaire["prénom"]
		
		return text

	def set_aide(self):
		"""
		Définit quelle genre d'aide les PNJ recevront.
		"""

		aide = adjuvant[randrange(len(adjuvant))]
	
		if aide == "personne" :
			self.pnj_aide =  self.generer_pnj_light()
			
			self.aide = "Les héros auront l'appui de " + description(self.pnj_aide)

		elif aide == "non" :
			self.aide =  "Les héros devront se débrouiller seuls."
		else : #"matériel"
			self.aide =  "Les héros se voient proposer une aide matérielle."


	def set_recompense(self):
		"""
		Génère une récompense en fonction de self.pnj_commanditaire.

		Assigne la valeur à self.recompense
		"""

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
			marchandises = list(self.pnj_commanditaire["métier"].split(" de/d' "))
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
		"""
		Assigne un metier a un personnage en fonction du commanditaire.

		Grâce à la classe personnage, génère un personnage qui exerce
		ce métier.

		Renvoie un dictionnaire contenant assez d'attributs pour décrire
		le personnage généré.  
		"""

		perso = Personnage()

		metier = poste_dans(self.commanditaire)
		perso.set_metier(metier)
		perso.set_particularites()
		return perso.pnj_light()


	def assembler_texte_de_quete(self):
		"""
		Renvoie dans le bon ordre, le texte des attributs formants
		le texte de quête.
		"""
		texte_de_quete = self.contexte_de_quete

		text = [
		# Déscription du pnj commanditaire :
		"Les héros rencontrent ", description(self.pnj_commanditaire), "\n",

		self.nomer_commanditaire()," souhaite les engager pour ", 

		# Description de la quête :
		self.quete,

		# Aide reçue :
		"\n", self.aide,

		# Récompense promise :
		"\n", self.nomer_commanditaire(), " propose de récompenser les héros ", 
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
			self.exclure_type_commanditaire("une organisation")
			self.quete += "__**voler**__ " + truc_a_voler()
			self.quete += qui_paye(self.generer_pnj_light(), self.type_commanditaire, self.commanditaire)
		
		elif self.type_quete == "infiltrer" :
			self.quete += "__**infiltrer**__ " + mission_infiltrer()
		
		elif self.type_quete == "protéger" :

			self.quete += "__**protéger**__ " + cible_protection()
		
		elif self.type_quete == "livrer" :
			self.quete += "__**livrer**__ " + cible_livraison()
			self.quete += qui_paye(self.generer_pnj_light(), self.type_commanditaire, self.commanditaire)
		
		elif self.type_quete == "enquêter" :
			victime = self.generer_pnj_light()
			self.quete += "__**enquêter**__ sur " + self.mission_enqueter(victime)
		
		elif self.type_quete == "kidnaper" :
			self.quete += "__**kidnaper**__ " + mission_kidnaper() + "\n"
			self.quete += qui_paye(self.generer_pnj_light(), self.type_commanditaire, self.commanditaire)
		
		elif self.type_quete == "tuer" :
			self.quete += "__**tuer**__ " + mission_tuer()

		elif self.type_quete == "détruire" :
			self.exclure_type_commanditaire("une organisation")
			self.quete += "__**détruire**__ " + mission_detruire()

		elif self.type_quete == "trouver" :
			self.quete += "__**trouver**__ "+ objet_precieux() + " dans " + lieu_quete()
			self.quete += "." + ou_nature()

		elif self.type_quete == "sauver" :
			personne = self.generer_pnj_light()
			self.set_commanditaire()
			self.quete += "__**sauver**__ " + description(personne)
			self.quete += "\nLes héros trouverons cette personne dans "
			self.quete += type_lieu_ville() + menace("une personne")

		elif self.type_quete == "fabriquer" :
			self.type_commanditaire = "une organisation"
			self.commanditaire = "le temple"
			self.quete += "__**fabriquer**__ " + mission_fabriquer()

		elif self.type_quete == "capturer" :
			self.type_commanditaire = "un réseau"
			self.commanditaire = "de braconnage"
			self.quete += "__**capturer**__ " + animal_sacre() + " dans " + lieu_quete_ext()
			self.quete += "." + ou_nature() + "\n"
			self.quete += qui_paye(self.generer_pnj_light(), self.type_commanditaire, self.commanditaire)
		
		elif self.type_quete == "empoisonner" :
			self.exclure_type_commanditaire("une organisation")
			self.quete += "__**empoisonner**__ " + mission_empoisonnement()

		elif self.type_quete == "intercepter" :
			self.quete += "__**intercepter**__ " + mission_intercepter()
		

	def mission_enqueter(self, victime):
		"""
		Le propos de l'enquête :
		un meurtre, un kidnaping, une organisation, un réseau, une personne, un vol.

		Modifie les attributs du commanditaire pour favoriser la cohérence.
		"""
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
			text += victime_morte(victime)
			text += "\nLe corps a été retrouvé " + scene_crime() + " "
			text += description_scene[randrange(len(description_scene))] + ".\n"
			text += "Le mobile est " + mobile[randrange(len(mobile))] + "."
			text += "\n\nLe coupable est " + genere_affiche_perso_light()
		
		elif raison == "un kidnaping" :
			text += "un kidnaping : \n\n"
			text += enquete_kidnaping(victime)
		
		elif raison == "une organisation" :
			self.type_commanditaire = "une organisation"
			self.commanditaire = organisation[randrange(len(organisation))]
			espion = self.generer_pnj_light()
			text += self.commanditaire + " :\n\nLes héros doivent démasquer un espion.\nC'est "
			text += genere_affiche_perso_light()
			
		elif raison == "une personne" :
			text += "une personne :\n\nIl s'agit de " + genere_affiche_perso_light()
		
		elif raison == "un vol" :
			text += "un vol :\n\nIl s'agit de " + truc_a_voler() + "\n\nLe coupable est "
			text += genere_affiche_perso_light()
		
		else : #"un réseau"
			nom_reseau = reseau[randrange(len(reseau))]
			text += "un réseau " + nom_reseau 
			text += ".\n\nLes héros doivent démasquer la tête pensante de ce réseau.\nC'est "
			metier = "le chef d'un réseau " + nom_reseau
			text += gen_perso_def_metier(metier)

		return text


	
