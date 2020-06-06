from random import randrange

from collection_de_mots.zone import *
from collection_de_mots.personnes import *
from collection_de_mots.activites import *
from collection_de_mots.trucs import *

from generer.nom import *

class Personnage:
	"""
	Définit les caractéristiques et attributs d'un PJ ou d'un PNJ d'après 
	les paramètres saisits par l'utilisateur.

	Associe les informations pour créer un texte d'ambiance décrivant
	le personnage.

	Renvoie ce texte.
	"""

	def __init__(self):
		"""
		caractéristiques des personnages.
		"""
		self.cmd_text = ""

		self.type = ""
		self.total_points = 0
		self.valeur_max = 0

		self.prenom = ""
		self.nom = ""
		self.age = ""
		self.race = ""
		self.genre = ""

		self.pronom = ""

		self.metier = ""
		self.leitmotiv = ""
		self.secret = ""
		self.ville = ""

		
		self.carac = {
			"Force" : 0,
			"Constitution" : 0,
			"Dextérité" : 0,
			"Intelligence" : 0,
			"Sagesse" : 0,
			"Charisme" : 0,
			}

		self.atout = "" # uniquement pour les PJ

		self.genre_proscrit = []
		self.races_proscrites = []
		self.metiers_proscrits = []



	def set_cmd_text(self, message):
		"""
		Découpe la saisie de l'utilisateur en paramètres utilisables
		et les index dans cmd_text.

		Les attributs proscrits, les attributs et Les caractéristiques
		commencent à patir de l'indice 3.
		"""
		self.cmd_text = list(message.split(","))
		for i in range(3, len(self.cmd_text), 1):
			self.cmd_text[i] = self.cmd_text[i].strip(" ")


	def set_type_de_personnage(self):
		"""
		Récupère le début de la commande saisie (index 0) qui indique le 
		type de personnage : PJ ou PNJ.
		"""
		type_de_perso = self.cmd_text[0].strip("!")
		self.type = type_de_perso.lower()

	def set_type_de_personnage_pj(self):
		"""
		assigne la valeur pj à self.type
		"""
		self.type = "pj"


	def set_total_points_et_valeur_max(self):
		"""
		Récupère l'index 1 et 2 de la commande saisie qui correspondent
		respectivement au total des points de caractéristiques à dépenser
		et au maximum de points à dépenser dans une caractéristique.

		Teste la validité de ces éléments et renvoie, si besoin un message
		d'erreur.
		"""
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
			if self.total_points < 1 or self.valeur_max < 1:
				return "Dans la commande :```!pj, x, y```x et y doivent être supérieurs à 1.", False
		except TypeError:
			return "Il manque peut être une virgule quelque part :```!pj, x, y, prénom=Toto``", False

		if self.total_points > self.valeur_max * 6:
			self.total_points = self.valeur_max * 6

		return "", True


	def set_param_identite(self):
		"""
		Découpe chaque paramètre en couple attribut + valeur.

		Lorsqu'un attribut a été définit par l'utilisateur,
		la valeur lui correspondant est enregistrée. 
		"""
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
		"""
		Pour 3 attributs : race, genre, métier, sans choisir la valeur
		de l'attribut en question, l'utilisateur peut définir des valeurs interdites.
		
		Ces valeurs sont stockées dans la liste correspondante.
		"""
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


	def set_particularites(self):
		"""
		Pour chaque attribut vide, on génère une valeur.

		Si cette valeur est interdite pour l'attribut en cours
		de génération, la fonction boucle sur elle même.

		Pour un PNJ on appelle la fonction metier_pers(), pour
		un Pj, on pioche dans la liste classe_pers.

		Les valeurs des attributs générés sont enregistrées.

		Un pronom est définit en fonction du genre du personnage.
		"""

		if self.race == "":
			race = pers_race[randrange(len(pers_race))][:-1]
			if race not in self.races_proscrites:
				self.race = race
			else :
				self.set_particularites()
			
		if self.genre == "":
			genre = pers_genre[randrange(len(pers_genre))]
			if genre not in self.genre_proscrit:
				self.genre = genre
			else:
				self.set_particularites()
				
		if self.metier == "":

			if self.type == "pj":
				metier_long =  classe_pers[randrange(len(classe_pers))]
			else :
				metier_long =  metier_pers()

			metier_court = self.raccourcir_nom_metier(metier_long)
			if metier_court not in self.metiers_proscrits:
				self.metier = metier_long
			else:
				self.set_particularites()

		if self.ville == "":
			self.ville = zone() + "\n"

		if self.secret == "":
			self.secret = "à propos " + pers_secret[randrange(len(pers_secret))]

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

		if self.genre == "masculin":
			self.pronom = "Il"

		elif self.genre == "féminin":
			self.pronom = "Elle"

		else:
			self.pronom = "Iel"


	def raccourcir_nom_metier(self, metier_long):
		"""
		Prend un nom de métier qui peut être composé de
		plusieurs mots.

		Coupe ce nom de métier aux espaces.

		Renvoie le premier mot sans espace.
		"""
		metier = metier_long.split(" ")
		metier_court = metier[0]

		if metier[0] == "apprenti/e" or metier[0] == "étudiant/e":
			metier_court = metier[1]
		return metier_court

	def bonus_de_metier(self):
		"""
		Cette fonction doit définir si le métier du personnage lui donne droit à 
		une caractéristique prioritaire.
		
		Appelle la fonction racourcir_metier.

		Le mot métier_court est comparé au dictionnaire : metiers_et_carac_associee.

		On utilise le plus petit nombre entre total_points et valeur_max
		pour générer nb_points aléatoire "bonus" à associer à la caractéristique
		prioritaire.

		Le nb_points est ajouté à la valeur de la caractéristique associé au métier.
		Le nb_points est ajouté au points_distribues.

		Appelle la fonction ajoute_1_dans_carac tant que points_distribues est
		inférieur au total_points.
		"""

		metier = self.raccourcir_nom_metier(self.metier)
		points_distribues = 0
		
		if self.valeur_max > self.total_points:
			bonus = self.total_points + 1
		else:
			bonus = self.valeur_max + 1

		nb_points = randrange(1, bonus)

		for k, v in metiers_et_carac_associee.items():
			if metier == k:				
				self.carac[v] += nb_points
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
		
		j = carac[randrange(len(carac))]

		if self.carac[j] < self.valeur_max:
			self.carac[j] += 1
		else:
			self.ajoute_1_dans_carac()


	def set_atout_pj(self):
		"""
		Appelle raccourcir_nom_metier.

		Pioche un atout pour le PJ dans la liste correspondant
		aux atouts de son métier.

		Si le métier du PJ ne correspond à aucun métier de la liste,
		pioche un atout générique en fin de liste.
		"""
		
		metier_court = self.raccourcir_nom_metier(self.metier)

		for i in range(len(classe_pers)):
			if metier_court == classe_pers[i]:
				atout = randrange(len(atouts_pj[i]))
				self.atout = atouts_pj[i][atout]
		if self.atout == "":
			atout = randrange(len(atouts_pj[14]))
			self.atout = atouts_pj[14][atout]



	def afficher_personnage(self):
		"""
		Mets en forme le texte qui sera renvoyé.

		Si le type de personnage est PJ, génère l'atout du PJ et l'ajoute
		au texte.

		Massage de Calliope + Attributs (+ Atout) + Caractéristiques.
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
		"\n", self.prenom, " souhaite plus que tout ", self.leitmotiv,
		"\n", self.pronom, " cache un secret " , self.secret, ".",
		"\nSa ville d'origine est " , self.ville, "\n"
		]

		if self.type == "pj":
			self.set_atout_pj()
			text += "Le principal atout de " + self.prenom + " est " + self.atout + ".\n\n"

		for k in self.carac.keys():
			text += k + " : " + str(self.carac[k]) + "\n"

		for i in range(len(text)):
			text_a_afficher += text[i]

		text_a_afficher += "\n\n*Comment personnaliser ce personnage ?*```!personnage```"

		return text_a_afficher


	def pnj_light(self):
		"""
		Renvoie les info d'un PNJ light.
		"""
		pnj_light = {
		"prénom" : self.prenom,
		"nom" : self.nom,
		"age" : self.age,
		"race" : self.race,
		"genre" : self.genre,
		"métier" :  self.metier,
		"pronom" : self.pronom,
		"secret" : self.secret,
		}
		
		return pnj_light


	def set_metier(self, metier):
		self.metier = metier