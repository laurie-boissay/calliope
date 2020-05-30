#!/usr/bin/python3.8
#coding:u8

from random import randrange

from collection_de_mots.quetes import *
from collection_de_mots.zone import *
from collection_de_mots.personnes import *
from collection_de_mots.activites import *
from collection_de_mots.trucs import *

from generation.generer_nom import *

"""
Définit une personne.
"""


def commanditaire_personne(commanditaire, quelle_orga):
	"""
	Donne plus de détail sur une personne faisant partie de 
	l'organisation ou du réseau commanditaire : 
	nom, prénom, age approximatif, genre, race, métier, secret.
	"""
	genre = pers_genre[randrange(len(pers_genre))]
	if genre == "féminin" :
		pronom = "elle"
		pronom_maj = "Elle"
	elif genre == "masculin" :
		pronom = "il"
		pronom_maj = "Il"
	else : # genre == "masculin" :
		pronom = "iel"
		pronom_maj = "Iel"

	race = pers_race[randrange(len(pers_race))]
	if commanditaire == "une organisation" :
		if quelle_orga == "le palais de justice" :

			metier = poste_palais_justice[randrange(len(poste_palais_justice))] + " au palais de justice"
		elif quelle_orga == "la caserne" :
			metier = poste_caserne[randrange(len(poste_caserne))] + " dans la caserne"
		elif quelle_orga == "La capitainerie" :
			metier = poste_capitainerie[randrange(len(poste_capitainerie))] + " dans la capitainerie"
		elif quelle_orga == "le chateau" :
			metier = poste_chateau[randrange(len(poste_chateau))] + " dans le chateau"
		elif quelle_orga == "le temple" :
			metier = poste_temple[randrange(len(poste_temple))] + " dans le temple"
		else : # la guilde des voleurs, marchands, assassins, prostituées, médecins
			metier = poste_guilde[randrange(len(poste_guilde))] + " de " + quelle_orga
	else : #commanditaire == "un réseau"
		metier = poste_guilde[randrange(len(poste_guilde))] + " de ce réseau " + quelle_orga

	phrase_1 = nom_pers(genre, race) + "."
	phrase_2 = "\nC'est une personne " + pers_age[randrange(len(pers_age))] + " de genre " + genre + ", de la race des "+race+"."
	phrase_3 = "\n" + pronom_maj +" est " + metier + "."
	phrase_4 = "\n" + pronom_maj + " cache un secret à propos "+ secret_personne() + "."

	return phrase_1 + phrase_2 + phrase_3 + phrase_4

def personne():
	"""
	Donne plus de détail sur une personne NE faisant PAS partie de 
	l'organisation ou du réseau commanditaire : 
	nom, prénom, age approximatif, genre, race, métier, secret.
	"""
	genre = pers_genre[randrange(len(pers_genre))]
	if genre == "féminin" :
		pronom = "elle"
		pronom_maj = "Elle"
	elif genre == "masculin" :
		pronom = "il"
		pronom_maj = "Il"
	else : # genre == "masculin" :
		pronom = "iel"
		pronom_maj = "Iel"

	race = pers_race[randrange(len(pers_race))]
	metier =  metier_pers()

	phrase_1 = nom_pers(genre, race) + "."
	phrase_2 = "\nC'est une personne " + pers_age[randrange(len(pers_age))] + " de genre " + genre + ", de la race des "+race+"."
	phrase_3 = "\n" + pronom_maj +" est " + metier + "."
	phrase_4 = "\n" + pronom_maj + " cache un secret à propos "+ secret_personne() + "."

	return phrase_1 + phrase_2 + phrase_3 + phrase_4


def nom_pers(genre, race) :
	"""
	Donne un nom et un prénom à la personne selon :
		- son genre ;
		- sa race.
	"""
	if genre == "féminin" :
		if race == "humains" or race == "humain":
			nom = prenoms_humains_f[randrange(len(prenoms_humains_f))] + " " + noms_humains[randrange(len(noms_humains))]
		elif race == "nains" or race == "nain" :
			nom = prenoms_nains_f[randrange(len(prenoms_nains_f))] + " " + noms_nains[randrange(len(noms_nains))]
		elif race == "elfes" or race == "elfe":
			nom = prenoms_elfes_f[randrange(len(prenoms_elfes_f))] + " " + noms_elfes[randrange(len(noms_elfes))]
		elif race == "orcs" or race == "orc":
			nom = prenoms_orcs_f[randrange(len(prenoms_orcs_f))] + " du-clan-de-" + prenoms_orcs_f[randrange(len(prenoms_orcs_f))]
		elif race == "demi-elfes" or race == "demi-elfe":
			nom = prenoms_elfes_f[randrange(len(prenoms_elfes_f))] + " " + noms_humains[randrange(len(noms_humains))]
		elif race == "demi-orcs" or race == "demi-orc":
			race = race_nom[randrange(len(race_nom))]
			if race == "orcs" or race == "orc":
				nom = prenoms_orcs_f[randrange(len(prenoms_orcs_f))] + " du-clan-de-" + prenoms_orcs_f[randrange(len(prenoms_orcs_f))]
			else : #humain
				nom = prenoms_humains_f[randrange(len(prenoms_humains_f))] + " " + noms_humains[randrange(len(noms_humains))]
		elif race == "halfelins" or race =="halfelin":
			nom = prenoms_halfelins_f[randrange(len(prenoms_halfelins_f))] + " " + noms_halfelins[randrange(len(noms_halfelins))]
		else : # "gnomes"
			nom = prenoms_gnomes_f[randrange(len(prenoms_gnomes_f))] + " " +noms_gnomes[randrange(len(noms_gnomes))]
	elif genre == "masculin" :
		if race == "humains" or race == "humain":
			nom = prenoms_humains_m[randrange(len(prenoms_humains_m))] + " " + noms_humains[randrange(len(noms_humains))] 
		elif race == "nains" or race == "nain":
			nom = prenoms_nains_m[randrange(len(prenoms_nains_m))] +" "+ noms_nains[randrange(len(noms_nains))]
		elif race == "elfes" or race == "elfe" :
			nom = prenoms_elfes_m[randrange(len(prenoms_elfes_m))] + " " + noms_elfes[randrange(len(noms_elfes))]
		elif race == "orcs" or race == "orc":
			nom =prenoms_orcs_m[randrange(len(prenoms_orcs_m))] + " du-clan-de-" + prenoms_orcs_m[randrange(len(prenoms_orcs_m))]
		elif race == "demi-elfes" or race == "demi-elfe":
			nom = prenoms_elfes_m[randrange(len(prenoms_elfes_m))] + " " + noms_humains[randrange(len(noms_humains))]
		elif race == "demi-orcs" or race == "demi-orc":
			race = race_nom[randrange(len(race_nom))]
			if race == "orcs" or race == "orc":
				nom = prenoms_orcs_m[randrange(len(prenoms_orcs_m))] + " du-clan-de-" + prenoms_orcs_m[randrange(len(prenoms_orcs_m))]
			else : #humain
				nom = prenoms_humains_m[randrange(len(prenoms_humains_m))] + " " + noms_humains[randrange(len(noms_humains))]
		elif race == "halfelins" or race == "halfelin":
			nom = prenoms_halfelins_m[randrange(len(prenoms_halfelins_m))] + " " + noms_halfelins[randrange(len(noms_halfelins))]
		else : # "gnomes"
			nom = prenoms_gnomes_m[randrange(len(prenoms_gnomes_m))] + " " +noms_gnomes[randrange(len(noms_gnomes))]
	else : #"andorgyne"
		genre = genre_nom[randrange(len(genre_nom))]
		return nom_pers(genre, race)
	return nom

def secret_personne() :
	"""
	Attibut un secret à la personne.
	"""
	return pers_secret[randrange(len(pers_secret))]


def metier_pers() :
	"""
	Pioche un métier pour la personne. 
	Précise pour certains métiers le domaine ou un nom de bâtiment.
	"""
	metier = pers_metier[randrange(len(pers_metier))]
	if metier == "haut-placé/e" :
		phrase_1 = metier + " dans " +organisation[randrange(len(organisation))]
	elif metier == "éleveur/éleveuse" :
		phrase_1 = metier + " de/d' " + animal_elevage[randrange(len(animal_elevage))]
	elif metier == "paysan/ne" :
		phrase_1 = metier + " dans la culture " + champ[randrange(len(champ))]
	elif metier == "servante/serviteur" :
		phrase_1 = metier+ " dans " + organisation[randrange(len(organisation))]
	elif metier == "serveur/serveuse" or metier == "tavernier/e" :
		phrase_1 = metier + " dans l'auberge " + nom_auberge()
	elif metier == "marchand/e" :
		phrase_1 = metier + " de/d' " +commerce[randrange(len(commerce))]
	elif metier == "capitaine" :
		phrase_1 = metier + " du bateau " + nom_navire()
	elif metier == "artisan/ne" :
		phrase_1 = metier + " " + artisanat[randrange(len(artisanat))]
	elif metier == "apprenti/e" :
		metier_appris = specialite()
		phrase_1 = metier + " " + metier_appris
	else :
		phrase_1 = metier
	return phrase_1

def specialite():
	metier = pers_metier[randrange(len(pers_metier))]
	if metier in pas_apprenti_e:
		return specialite()
	else:
		return metier