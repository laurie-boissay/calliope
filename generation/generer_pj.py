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
	message = message.strip("!")
	message = list(message.split(" "))

	arguments = {}

	nb_points_de_carac = message[1]
	valeur_max = message[2]
	
	for i in range(3, len(message), 1):
		couple = message[i].split("=")
		arguments[couple[0]] = couple[1]
		
	return reroll(nb_points_de_carac, valeur_max, **arguments)
	

def reroll(nb_points_de_carac, valeur_max, **kwargs):

	text_pj = ""

	pj = {
	'prénom' : "",
	'nom' : "",
	'age' : "",
	'race' : "",
	'métier' : "",
	'genre' : "",
	'secret' : "",
	'ville' : "",
	}

	for k, v in kwargs.items():
		for key, value in pj.items():
			if key == k:
				pj[key] = v

	if pj["race"] == "":
		pj["race"] = race = pers_race[randrange(len(pers_race))]
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
		text_pj += k + " : " + v + "\n"
	# Ajouter une fonction pour distribuer les points de carac.
	return text_pj