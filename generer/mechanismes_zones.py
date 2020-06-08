from random import randrange


from collection_de_mots.zone import *
from collection_de_mots.activites import *


def make_good_number(candidate_number, min, max):
	integer, number = is_it_int(candidate_number)

	if not integer:
		number = randrange(min, max)

	in_interval = is_it_in_interval(number, min, max)

	if not in_interval:
		number = randrange(min, max)

	return number

		
def is_it_int(candidate_number):
	try :
		candidate_number = int(candidate_number)
		return True, candidate_number
	except ValueError:
		return False, candidate_number


def is_it_in_interval(number, min, max):

	if number > max or number < min:
		return False
	else:
		return True


def zone_attribut_avec_indice(attribut, liste_correpondante):

	if attribut not in liste_correpondante:
		number = make_good_number(attribut, 1, len(liste_correpondante))

		for i in range(len(liste_correpondante)):
			if number-1 == i:
				attribut = liste_correpondante[i]

	return  attribut, number


def nom_zone(taille, rich, densite, activite):
	"""
	Génère un nom de zone selon :
		- la taille de la zone ;
		- La densité de population de la zone ;
		- la richesse des habitants ;
		- l'activité pricipale.
	"""
	if taille == "très petite (1/5)" or taille == "petite (2/5)" :
		if densite == "tranquille (population faible)" or densite == "déserte (population rare)" :
			phrase_1 = "le "
			phrase_3 = "hammeau "
		elif densite == "très peuplée" :
			phrase_1 = "la "
			phrase_3 = "bourgade "
		else : # densite == "surpeuplée" :
			phrase_1 = "La "
			phrase_3 = "ville "

	elif taille == "grande (3/5)" or taille == "très grande (4/5)" :
		if densite == "déserte (population rare)" :
			phrase_1 = "La "
			phrase_3 = "étendue "
		elif densite == "tranquille (population faible)" :
			phrase_1 = "le "
			phrase_3 = "village "
		elif densite == "très peuplée" :
			phrase_1 = "la "
			phrase_3 = "ville "
		else : # densite == "surpeuplée" :
			phrase_1 = "la "
			phrase_3 = "citée "

	else : #taille == "immense (5/5)" :
		if densite == "déserte (population rare)" or densite == "tranquille (population faible)" :
			phrase_1 = "la "
			phrase_3 = "étendue "
		elif densite == "très peuplée" :
			phrase_1 = "la "
			phrase_3 = "citée "
		else : # densite == "surpeuplée" :
			phrase_1 = "la "
			phrase_3 = "mégapole "

	if rich == "misérable" :
		phrase_2 = "misérable "
	elif rich == "pauvre" :
		phrase_2 = "modeste "
	elif rich == "plutôt à l'aise financièrement" :
		phrase_2 = "magnifique "
	else : #"riche"
		if taille != "très petite (1/5)" and taille != "petite (2/5)" and densite != "déserte (population rare)" and densite != "tranquille (population faible)" :
			phrase_2 = "majestueux/se "
		else :
			phrase_2 = "joli/e "

	if activite == "le commerce" :
		phrase_4 = commercants[randrange(len(commercants))]
	elif activite == "l'esclavage" :
		phrase_4 = esclavage[randrange(len(esclavage))]
	elif activite == "la religion" :
		phrase_4 = religion[randrange(len(religion))]
	elif activite == "la magie" :
		phrase_4 = magie[randrange(len(magie))]
	elif activite == "la contrebande" :
		phrase_4 = "franc/he"
	elif activite == "l'élevage" :
		phrase_4 = eleveurs[randrange(len(eleveurs))]
	elif activite == "l'alcool" :
		phrase_4 = alcool[randrange(len(alcool))]
	elif activite == "la drogue" :
		phrase_4 = drogue[randrange(len(drogue))]
	elif activite == "la pêche" :
		phrase_4 = "des pêcheurs"
	elif activite == "la chasse" :
		phrase_4 = chasse[randrange(len(chasse))]
	elif activite == "l'agriculture" :
		phrase_4 = "des champs verts"
	elif activite == "l'artisanat" :
		phrase_4 = artisants[randrange(len(artisants))]
	else : #activite == "extraction minière" :
		phrase_4 = matiere_extraite[randrange(len(matiere_extraite))]
	
	return phrase_1 + phrase_2 + phrase_3 + phrase_4


