from random import randrange

from generation.generer_personne import *
from generation.generer_quete import *


from collection_de_mots.zone import *
from collection_de_mots.personnes import *
from collection_de_mots.activites import *
from collection_de_mots.trucs import *

class Personnage:

	def __init__(self):
		self.cmd_text = ""

		self.type = ""
		self.total_points = 0
		self.valeur_max = 0

		self.prenom = ""
		self.nom = ""
		self.age = ""
		self.race = ""
		self.genre = ""

		self.metier = ""
		self.leitmotiv = ""
		self.secret = ""
		self.ville = ""

		self.force = 0
		self.dexterite = 0
		self.intelligence = 0
		self.sagesse = 0
		self.charisme = 0

		self.genre_proscrit = []
		self.races_proscrites = []
		self.metiers_proscrits = []


	def set_cmd_text(self, message):
		self.cmd_text = list(message.split(","))
		for i in range(3, len(self.cmd_text), 1):
			self.cmd_text[i] = self.cmd_text[i].strip(" ")


	def set_type_de_personnage(self):
		type_de_perso = self.cmd_text[0].strip("!")
		self.type = type_de_perso.lower()

	def set_total_points_et_valeur_max(self):
		try :
			self.total_points = self.cmd_text[1]	
			self.valeur_max = self.cmd_text[2]
		except IndexError:
			text = [
			"Il manque peut être une virgule après !pj\n"
			"Ou tu n'as pas précisé les paramètres obligatoires juste après !pj,"
			" ```!pj, 8, 2 ```"
			]
			return text[0], False

		try :
			self.total_points = int(self.total_points)
			self.valeur_max = int(self.valeur_max)

		except ValueError:
			text = [
			"Tu as peut être oublié une virgule entre les paramètres.\n"
			"Ou les paramètres valeur max et points de carac ne sont pas des nombres."
			"```!pj, 8, 2, métier=druide```"
			]
			return text[0], False

		try:
			if self.total_points < 0 or self.valeur_max < 0:
				return "Dans la commande :```!pj, x, y```x et y doivent être positifs.", False
		except TypeError:
			return "Il manque peut être une virgule quelque part :```!pj, x, y, prénom=Toto``", False

		return "", True


	def set_param_identite(self):
		for i in range(3, len(self.cmd_text), 1):

			if "=" in self.cmd_text[i]:
				couple = self.cmd_text[i].split("=")
				couple[0] = couple[0].strip(" ")
				couple[1] = couple[1].strip(" ")
				if couple[0] == "prénom":
					self.prenom = couple[1]
				elif couple[0] == "nom":
					self.nom = couple[1]
				elif couple[0] == "age":
					self.age = couple[1]
				elif couple[0] == "race":
					self.race = couple[1].lower()
				elif couple[0] == "genre":
					self.genre = couple[1].lower()
				elif couple[0] == "métier":
					self.metier = couple[1].lower()
				elif couple[0] == "leitmotiv":
					self.leitmotiv = couple[1]
				elif couple[0] == "secret":
					self.secret = couple[1]
				elif couple[0] == "ville":
					self.ville = couple[1]


	def set_param_proscrits(self):
		for i in range(3, len(self.cmd_text), 1):

			if "_"in self.cmd_text[i]:
				couple = self.cmd_text[i].split("_")
				couple[0] = couple[0].strip(" ")
				couple[1] = couple[1].strip(" ")
				if couple[0] == "race":
					self.races_proscrites.append(couple[1])
				elif couple[0] == "genre":
					self.genre_proscrit.append(couple[1])
				elif couple[0] == "métier":
					self.metiers_proscrits.append(couple[1])


	def generer_particularites(self):

		if self.race == "":
			race = pers_race[randrange(len(pers_race))][:-1]
			if race not in self.races_proscrites:
				self.race = race
			else :
				self.generer_particularites()
			
		if self.genre == "":
			genre = pers_genre[randrange(len(pers_genre))]
			if genre not in self.genre_proscrit:
				self.genre = genre
			else:
				self.generer_particularites()
				
		if self.metier == "":

			if self.type == "pj":
				metier_long =  classe_pers[randrange(len(classe_pers))]
			else :
				metier_long =  metier_pers[randrange(len(metier_pers))]

			metier_court = self.raccourcir_nom_metier(metier_long)
			if metier_court not in self.metiers_proscrits:
				self.metier = metier_long
			else:
				self.generer_particularites()

		if self.ville == "":
			self.ville = zone() + "\n"

		if self.secret == "":
			self.secret = "à propos " + secret_personne()

		if self.prenom == "":
			denomination = nom_pers(self.genre, self.race).split(" ")
			self.prenom = denomination[0]

		if self.nom == "":
			denomination = nom_pers(self.genre, self.race).split(" ")
			self.nom = denomination[1]

		if self.age == "":
			self.age = pers_age[randrange(len(pers_age))]

		if self.leitmotiv == "":
			self.leitmotiv = leitmotiv[randrange(len(leitmotiv))]


	def raccourcir_nom_metier(self, metier_long):
		metier = metier_long.split(" ")
		metier_court = metier[0]
		return metier_court

	def bonus_de_metier(self):
		"""
		Cette fonction doit définir si le métier du pj lui donne droit à 
		une caractéristique prioritaire.
		
		Appelle la fonction racourcir_metier

		Le mot métier_court ainsi préparé est comparé au dictionnaire : metiers_et_carac_associee.

		On utilise le plus petit nombre entre nb_points_de_carac et valeur_max
		pour générer un nombre aléatoire de points "bonus" à associer à la caractéristique
		prioritaire.

		Appelle la fonction ajoute_1_dans_carac tant que points_distribues est
		inférieur au nb_points_de_carac.

		Renvoit les caractéristiques du perso généré ainsi que leur valeur.
		"""

		metier = self.raccourcir_nom_metier(self.metier)
		points_distribues = 0
		
		if self.valeur_max > self.total_points:
			bonus = self.total_points + 1
		else:
			bonus = self.valeur_max + 1

		for k, v in metiers_et_carac_associee.items():
			if metier == k:
				nb_points = randrange(1, bonus)

				if v == "Force":
					self.force += nb_points
					print(v, " : ", str(self.force))

				elif v == "Dextérité":
					self.dexterite += nb_points
					print(v, " : ", str(self.dexterite))

				elif v == "Intelligence":
					self.intelligence += nb_points
					print(v, " : ", str(self.intelligence))

				elif v == "Sagesse":
					self.sagesse += nb_points
					print(v, " : ", str(self.sagesse))

				else:				
					self.charisme += nb_points
					print(v, " : ", str(self.charisme))
					
				points_distribues += nb_points

		while points_distribues < self.total_points:
			self.ajoute_1_dans_carac()
			points_distribues += 1


	def ajoute_1_dans_carac(self):
		"""
		Ajoute 1 point dans une caractéristique aléatoire si valeur_max
		n'est pas atteinte.

		Si valeur_max est déjà atteinte, la fonction boucle sur elle même.
		"""	
		text = ""
		j = randrange(5)
		print("j : ", j)

		if j == 0:
			if self.force < self.valeur_max:
				self.force += 1
			else :
				self.ajoute_1_dans_carac()
		
		elif j == 1:
			if self.dexterite < self.valeur_max:
				self.dexterite += 1
			else :
				self.ajoute_1_dans_carac()

		elif j == 2:
			if self.intelligence < self.valeur_max:
				self.intelligence += 1
			else :
				self.ajoute_1_dans_carac()

		elif j == 3:
			if self.sagesse < self.valeur_max:
				self.sagesse += 1
			else :
				self.ajoute_1_dans_carac()
		else:
			if self.charisme < self.valeur_max:
				self.charisme += 1
			else :
				self.ajoute_1_dans_carac()
			

	def afficher_personnage(self):
		"""
		print(self.genre)
		print(self.races_proscrites)
		print(self.metiers_proscrits)
		print(self.type)
		print(self.total_points)
		print(self.valeur_max)
		"""

		text_a_afficher = ""
		text = [
		"J'ai façonné un personnage qui pourrait correspondre à tes attentes.\n"
		"Pense à le sauvegarder s'il te convient :\n",

		"\nPrénom : " , self.prenom,
		"\nNom : " , self.nom,
		"\nAge : " , self.age,
		"\nRace : " , self.race,
		"\nGenre : " , self.genre,

		"\n\nMétier : " , self.metier,
		"\nLeitmotiv : " , self.leitmotiv,
		"\nSecret : " , self.secret,
		"\nVille d'origine : " , self.ville,

		"\nForce : " , str(self.force),
		"\nDextérité : " , str(self.dexterite),
		"\nIntelligence : " , str(self.intelligence),
		"\nSagesse : " , str(self.sagesse),
		"\nCharisme : " , str(self.charisme),
		]

		for i in range(len(text)):
			text_a_afficher += text[i]

		return text_a_afficher