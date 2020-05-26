#!/usr/bin/python3.8
#coding:u8

from menu import *


from collection_de_mots.quetes import *
from collection_de_mots.zone import *
from collection_de_mots.personnes import *
from collection_de_mots.activites import *
from collection_de_mots.trucs import *

def nom_auberge() :
	return hasard(auberge_nom) + " " + hasard(auberge_adj)

def nom_navire() :
	return hasard(navire_nom) + " " + hasard(navire_adj)

def objet_precieux() :
	return hasard(objet_nom) + " " + hasard(objet_adj)

def lieu_quete() :
	return hasard(lieu_quete_nom) + " " + hasard(lieu_quete_adj)

def lieu_quete_ext() :
	return hasard(ext_nom) + " " + hasard(ext_adj)

def animal_sacre():
	return "le/l' "+hasard(animal_sauvage) + " " + hasard(objet_adj)

def zone() :
	activite_1 = hasard(activite)
	activite_2 = hasard(activite)
	taille = hasard(superficie)
	rich = hasard(richesse)
	temp = hasard(climat)
	pop = hasard(quantite_pop)

	if activite_1 == activite_2 :
		return zone()
	else :	
		phrase_0 = nom_zone(taille, rich, pop, activite_1)+"."
		phrase_1 = "C'est une "+taille+" zone "+pop+"."
		if taille == "très grande (4/5)" or taille == "immense (5/5)" :
			if pop == "surpeuplée" or pop == "très peuplée" :
				phrase_2 = " La population est cosmopolite."
			else :
				phrase_2 = habitants()
		else :
			phrase_2 = habitants()

		phrase_3 = "L'activité principale est "+activite_1+", l'activité secondaire est "+activite_2+"."
		phrase_4 = "La population est "+rich+". Le climat est "+temp+". La zone est "+hasard(paysage)+"."
		return  phrase_0+"\n\n"+phrase_1 + phrase_2 +"\n"+ phrase_3 +"\n"+ phrase_4 +"\n"

def habitants():
	race_1 = hasard(pers_race)
	race_2 = hasard(pers_race)
	if race_1 == race_2 :
		return habitants()
	else :
		return " Habitée mojoritairement par des "+race_1+". Il y a aussi quelques "+race_2+"."

def nom_zone(taille, rich, pop, activite_1):
	if taille == "très petite (1/5)" or taille == "petite (2/5)" :
		if pop == "tranquille (population faible)" or pop == "déserte (population rare)" :
			phrase_1 = "le "
			phrase_3 = "hammeau "
		elif pop == "très peuplée" :
			phrase_1 = "la "
			phrase_3 = "bourgade "
		else : # pop == "surpeuplée" :
			phrase_1 = "La "
			phrase_3 = "ville "

	elif taille == "grande (3/5)" or taille == "très grande (4/5)" :
		if pop == "déserte (population rare)" :
			phrase_1 = "La "
			phrase_3 = "étendue "
		elif pop == "tranquille (population faible)" :
			phrase_1 = "le "
			phrase_3 = "village "
		elif pop == "très peuplée" :
			phrase_1 = "la "
			phrase_3 = "ville "
		else : # pop == "surpeuplée" :
			phrase_1 = "la "
			phrase_3 = "citée "

	else : #taille == "immense (5/5)" :
		if pop == "déserte (population rare)" or pop == "tranquille (population faible)" :
			phrase_1 = "la "
			phrase_3 = "étendue "
		elif pop == "très peuplée" :
			phrase_1 = "la "
			phrase_3 = "citée "
		else : # pop == "surpeuplée" :
			phrase_1 = "la "
			phrase_3 = "mégapole "

	if rich == "misérable" :
		phrase_2 = "misérable "
	elif rich == "pauvre" :
		phrase_2 = "modeste "
	elif rich == "plutôt à l'aise financièrement" :
		phrase_2 = "magnifique "
	else : #"riche"
		if taille != "très petite (1/5)" and taille != "petite (2/5)" and pop != "déserte (population rare)" and pop != "tranquille (population faible)" :
			phrase_2 = "majestueux/se "
		else :
			phrase_2 = "joli/e "

	if activite_1 == "le commerce" :
		phrase_4 = hasard(commercants)
	elif activite_1 == "l'esclavage" :
		phrase_4 = hasard(esclavage)
	elif activite_1 == "la religion" :
		phrase_4 = hasard(religion)
	elif activite_1 == "la magie" :
		phrase_4 = hasard(magie)
	elif activite_1 == "la contrebande" :
		phrase_4 = "franc/he"
	elif activite_1 == "l'élevage" :
		phrase_4 = hasard(eleveurs)
	elif activite_1 == "l'alcool" :
		phrase_4 = hasard(alcool)
	elif activite_1 == "la drogue" :
		phrase_4 = hasard(drogue)
	elif activite_1 == "la pêche" :
		phrase_4 = "des pêcheurs"
	elif activite_1 == "la chasse" :
		phrase_4 = hasard(chasse)
	elif activite_1 == "l'agriculture" :
		phrase_4 = "des champs verts"
	elif activite_1 == "l'artisanat" :
		phrase_4 = hasard(artisants)
	else : #activite_1 == "extraction minière" :
		phrase_4 = hasard(matiere_extraite)
	return phrase_1 + phrase_2 + phrase_3 + phrase_4
