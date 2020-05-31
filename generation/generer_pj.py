from random import randrange

from generation.generer_quete import *

from collection_de_mots.zone import *
from collection_de_mots.personnes import *
from collection_de_mots.activites import *
from collection_de_mots.trucs import *

"""
Génère un héro/une héroïne ou un PNJ.
"""

arguments = {}

def arguments_reroll(message):
	"""
	Sépare la commande en paramètres de commande.

	Renvoit un message d'erreur si les paramètres obligatoires
	ne peuvent être utilisés.

	Appelle la fonction make_int.

	Appelle la fonction découpage_en_arguments.

	Appelle la fonction reroll.

	Renvoit les caractéristiques et particularités du PJ généré et leur valeur.
	"""
	for k in arguments.keys():
		arguments[k] = ""

	message = list(message.split(","))

	for i in range(3, len(message), 1):
		message[i] = message[i].strip(" ")

	try :
		nb_points_de_carac = message[1]	
		valeur_max = message[2]
	except IndexError:
		text = [
		"Il manque peut être une virgule après !pj\n"
		"Ou tu n'as pas précisé les paramètres obligatoires juste après !pj,"
		" ```!pj, 8, 2 ```"
		]
		return text[0]

	nb_points_de_carac = make_int(nb_points_de_carac)
	valeur_max = make_int(valeur_max)

	genre_proscrit, races_proscrites, metiers_proscrits = découpage_en_arguments(message)
	
	return reroll(nb_points_de_carac, valeur_max, genre_proscrit, races_proscrites, metiers_proscrits, **arguments)


def découpage_en_arguments(message):
	"""
	Prend les paramètres listés dans message 
		si le paramètre contient le symbole = :
			découpe le paramètre en arguments et les stocke 
			dans le dictionnaire arguments.
		si le paramètre contient le symbole _ :
			récupère les mots proscrits par l'utilisateur et
			les stock dans la liste adaptée.

	Renvoit les listes : genre_proscrit, races_proscrites, metiers_proscrits
	"""
	genre_proscrit = []
	races_proscrites = []
	metiers_proscrits = []

	for i in range(3, len(message), 1):

		if "=" in message[i]:
			couple = message[i].split("=")
			couple[0]=couple[0].strip(" ")
			couple[1]=couple[1].strip(" ")
			arguments[couple[0]] = couple[1]

		elif "_"in message[i]:
			couple = message[i].split("_")
			couple[0]=couple[0].strip(" ")
			couple[1]=couple[1].strip(" ")
			if couple[0] == "race":
				races_proscrites.append(couple[1])
			elif couple[0] == "genre":
				genre_proscrit.append(couple[1])
			elif couple[0] == "métier":
				metiers_proscrits.append(couple[1])
	
	return genre_proscrit, races_proscrites, metiers_proscrits
		

def reroll(nb_points_de_carac, valeur_max, genre_proscrit, races_proscrites, metiers_proscrits, **kwargs):
	"""
	Vérifie que nb_points_de_carac, valeur_max sont positifs et renvoie
	un message d'erreur si ce n'est pas le cas.

	Réinitialise les valeurs du dictionnaire qui stock les paramètres.
	Verifie pour chaque paramètre si l'utilisateur a définit une valeur.
	les valeurs définies par l'utilisateur sont envoyé dans le dictionnaire PJ.

	Appelle la fonction generer_particularites.

	Renvoit les caractéristiques et particularités du PJ généré et leur valeur.
	"""
	text_pj = [
	"J'ai façonné un personnage qui pourrait correspondre à tes attentes.\n"
	"Pense à le sauvegarder s'il te convient :\n\n"
	]

	erreur_nb_neg = [
		"Dans la commande :"
		"```!pj, x, y```"
		"x et y doivent être positifs."
		]

	try:
		if nb_points_de_carac < 0 or valeur_max < 0:
			return erreur_nb_neg[0]
	except TypeError:
		return "Il manque peut être une virgule quelque part :```!pj, x, y, prénom=Toto``"

	for k in pj.keys():
		pj[k] = ""

	for k in kwargs.keys():
		for key in pj.keys():
			if key == k:
				pj[key] = kwargs[k].lower()

	generer_particularites(genre_proscrit, races_proscrites, metiers_proscrits)

	for k, v in pj.items(): # afficher le tableau PJ.
		text_pj[0] += k + " : " + v + "\n"

	text_pj[0] += distribuer_points_carac(nb_points_de_carac, valeur_max, pj["métier"])
	return text_pj[0]


def generer_particularites(genre_proscrit, races_proscrites, metiers_proscrits):
	"""
	Génère des valeurs pour les paramètres laissés vide par l'utilisateur.

	Et vérifie que la valeur générée ne fait pas partie d'une liste d'interdits.
	"""

	if pj["race"] == "":
		race = pers_race[randrange(len(pers_race))][:-1]
		if race not in races_proscrites:
			pj["race"] = race
		else :
			generer_particularites(genre_proscrit, races_proscrites, metiers_proscrits)
		
	if pj["genre"] == "":
		genre = pers_genre[randrange(len(pers_genre))]
		if genre not in genre_proscrit:
			pj["genre"] = genre
		else:
			generer_particularites(genre_proscrit, races_proscrites, metiers_proscrits)
			
	if pj["métier"] == "":
		metier_long =  metier_pers()
		metier_court = racourcir_metier(metier_long)
		if metier_court not in metiers_proscrits:
			pj["métier"] = metier_long
		else:
			generer_particularites(genre_proscrit, races_proscrites, metiers_proscrits)

	if pj["ville"] == "":
		pj["ville"] = zone() + "\n"

	if pj["secret"] == "":
		pj["secret"] = "à propos " + secret_personne()

	if pj["prénom"] == "":
		denomination = nom_pers(pj["genre"], pj["race"]).split(" ")
		pj["prénom"] = denomination[0]

	if pj["nom"] == "":
		denomination = nom_pers(pj["genre"], pj["race"]).split(" ")
		pj["nom"] = denomination[1]

	if pj['age'] == "":
		pj['age'] = pers_age[randrange(len(pers_age))]

	if pj['leitmotiv'] == "":
		pj['leitmotiv'] = leitmotiv[randrange(len(leitmotiv))]


def racourcir_metier(metier):
	"""
	Découpe le nom de métier et ne garder que le premier
	mot sans espace.

	Mets le nom de métier en minuscule.

	Renvoit le métier raccourci.
	"""
	metier = metier.split(" ")
	metier[0] = metier[0].lower()

	return metier[0]


def make_int(number):
	"""
	Essai de tranformer une str en int.

	Renvoit un message d'erreur si le nombre ne peut être
	transformé.

	ou renvoit le nombre.
	"""

	try :
		number = int(number)

	except ValueError:
		text = [
		"Tu as peut être oublié une virgule entre les paramètres."
		" ```!pj, 8, 2, métier=druide```"
		]
		return text[0]

	return(number)


def distribuer_points_carac(nb_points_de_carac, valeur_max, metier_long):
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
	text = ""
	metier = racourcir_metier(metier_long)
	points_distribues = 0
	bonus = valeur_max + 1
	if valeur_max > nb_points_de_carac:
		bonus = nb_points_de_carac +1

	for k, v in carac_et_points.items():
		carac_et_points[k] = 0

	for k, v in metiers_et_carac_associee.items():
		if metier == k:
			nb_points = randrange(1, bonus)
			carac_et_points[v] += nb_points
			points_distribues += nb_points

	while points_distribues < nb_points_de_carac:
		ajoute_1_dans_carac(valeur_max)
		points_distribues += 1

	for k, v in carac_et_points.items():
		text += k + " : " + str(v) + "\n"

	return text

def ajoute_1_dans_carac(valeur_max):
	"""
	Ajoute 1 point dans une caractéristique aléatoire si valeur_max
	n'est pas atteinte.

	Si valeur_max est déjà atteinte, la fonction boucle sur elle même.
	"""	
	j = carac[randrange(len(carac))]
	if carac_et_points[j] < valeur_max:
		carac_et_points[j] += 1
	else :
		return ajoute_1_dans_carac(valeur_max)


