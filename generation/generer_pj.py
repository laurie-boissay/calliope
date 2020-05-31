from random import randrange

from generation.generer_quete import *

from collection_de_mots.zone import *
from collection_de_mots.personnes import *
from collection_de_mots.activites import *
from collection_de_mots.trucs import *

"""
Génère un héro/une héroïne ou un PNJ.
"""

def arguments_reroll(message):
	"""
	Récupère la commande et la traduit en arguments
	pour la fonction reroll.

	Renvoit un message d'erreur si les arguments obligatoires
	ne peuvent être utilisés.

	Appelle la fonction make_int.

	Appelle la fonction reroll.

	Renvoit les caractéristiques et particularités du PJ généré et leur valeur.
	"""
	message = list(message.split(","))
	arguments = {}

	for i in range(3, len(message), 1):
		message[i] = message[i].strip(" ")

	try :
		nb_points_de_carac = message[1]	
		valeur_max = message[2]
	except IndexError:
		text = [
		"Il manque peut être une virgule après !pj.\n"
		"Ou tu n'as pas précisé les paramètres obligatoires. Ex :"
		" ```!pj, 8, 2 ```"
		]
		return text[0]
	
	for i in range(3, len(message), 1):
		couple = message[i].split("=")
		couple[0]=couple[0].strip(" ")
		couple[1]=couple[1].strip(" ")
		arguments[couple[0]] = couple[1]

	nb_points_de_carac = make_int(nb_points_de_carac)
	valeur_max = make_int(valeur_max)
	
	return reroll(nb_points_de_carac, valeur_max, **arguments)
	

def reroll(nb_points_de_carac, valeur_max, **kwargs):
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

	if nb_points_de_carac < 0 or valeur_max < 0:
		return erreur_nb_neg[0]

	for k, v in pj.items():
		pj[k] = ""

	for k, v in kwargs.items():
		for key, value in pj.items():
			if key == k:
				pj[key] = v

	generer_particularites()

	for k, v in pj.items(): # afficher le tableau PJ.
		text_pj[0] += k + " : " + v + "\n"

	text_pj[0] += distribuer_points_carac(nb_points_de_carac, valeur_max, pj["métier"])
	return text_pj[0]


def generer_particularites():
	"""
	Génère des valeurs pour les paramètres
	laissés vide par l'utilisateur.
	"""

	if pj["race"] == "":
		pj["race"] = pers_race[randrange(len(pers_race))][:-1]
	else:
		pj["race"] = pj["race"].lower()
		
	if pj["genre"] == "":
		pj["genre"] = genre = pers_genre[randrange(len(pers_genre))]
	else:
		pj["genre"] = pj["genre"].lower()
			
	if pj["métier"] == "":
		pj["métier"] = metier_pers()

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


def distribuer_points_carac(nb_points_de_carac, valeur_max, metier):
	"""
	Cette fonction doit définir si le métier du pnj lui donne droit à 
	une caractéristique prioritaire.

	Pour cela il faut découper le nom de métier et ne garder que le premier
	mot sans espace.

	Le mot métier ainsi préparé est comparé au dictionnaire : metiers_et_carac_associee.

	On utilise le plus petit nombre entre nb_points_de_carac et valeur_max
	pour générer un nombre aléatoire de points "bonus" à associer à la caractéristique
	prioritaire.

	Appelle la fonction ajoute_1_dans_carac tant que points_distribues est
	inférieur au nb_points_de_carac.

	Renvoit les caractéristiques du perso généré ainsi que leur valeur.
	"""
	
	text = ""
	metier = metier.split(" ")
	metier[0] = metier[0].lower()
	points_distribues = 0

	bonus = valeur_max + 1
	if valeur_max > nb_points_de_carac:
		bonus = nb_points_de_carac +1

	for k, v in carac_et_points.items():
		carac_et_points[k] = 0

	for k, v in metiers_et_carac_associee.items():
		if metier[0] == k:
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


