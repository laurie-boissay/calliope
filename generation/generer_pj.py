from random import randrange

from generation.generer_quete import *

from collection_de_mots.zone import *
from collection_de_mots.personnes import *
from collection_de_mots.activites import *
from collection_de_mots.trucs import *

"""
Génère un héro ou une héroïne.
"""

def arguments_reroll(message):
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
	
	return reroll(nb_points_de_carac, valeur_max, **arguments)
	

def reroll(nb_points_de_carac, valeur_max, **kwargs):
	text_pj = [
	"J'ai façonné un personnage qui pourrait correspondre à tes attentes.\n"
	"Pense à le sauvegarder s'il te convient :\n\n"
	]

	for k, v in pj.items():
		pj[k] = ""

	for k, v in kwargs.items():
		for key, value in pj.items():
			if key == k:
				pj[key] = v

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

	for k, v in pj.items(): # afficher le tableau PJ.
		text_pj[0] += k + " : " + v + "\n"

	try :
		nb_points_de_carac = int(nb_points_de_carac)
		valeur_max = int(valeur_max)
	except ValueError:
		text = [
		"Tu as peut être oublié une virgule entre les paramètres."
		" ```!pj, 8, 2, métier=druide```"
		]
		return text[0]

	text_pj[0] += distribuer_points_carac(nb_points_de_carac, valeur_max, pj["métier"])
	return text_pj[0]


def distribuer_points_carac(nb_points_de_carac, valeur_max, metier):
	
	text = ""
	metier = metier.split(" ")
	metier[0] = metier[0].lower()
	points_distribues = 0

	for k, v in carac_et_points.items():
		carac_et_points[k] = 0

	for k, v in metiers_et_carac_associee.items():
		if metier[0] == k:
			nb_points = randrange(1, valeur_max+1)
			carac_et_points[v] += nb_points
			points_distribues += nb_points

	while points_distribues < nb_points_de_carac:
		ajoute_1_dans_carac(nb_points_de_carac, valeur_max)
		points_distribues += 1

	for k, v in carac_et_points.items():
		text += k + " : " + str(v) + "\n"

	return text

def ajoute_1_dans_carac(nb_points_de_carac, valeur_max):	
	j = carac[randrange(len(carac))]
	if carac_et_points[j] < valeur_max:
		carac_et_points[j] += 1
	else :
		return ajoute_1_dans_carac(nb_points_de_carac, valeur_max)


