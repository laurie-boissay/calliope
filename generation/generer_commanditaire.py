#!/usr/bin/python3.8
#coding:u8

from menu import *

from generation.generer_quete import *

from collection_de_mots.quetes import *
from collection_de_mots.zone import *
from collection_de_mots.personnes import *
from collection_de_mots.activites import *
from collection_de_mots.trucs import *

def generer_commanditaire() :
	payeur = hasard(commanditaire)
	phrase_1 = "\nLes héros sont approchés par "

	if payeur == "une organisation" :
		quelle_orga = hasard(organisation)
		une_personne = commanditaire_personne("une organisation", quelle_orga)		
		phrase_2 = quelle_orga + " en la personne de " + une_personne
		phrase_3 = choix_quete("une organisation", quelle_orga)
		phrase_4 = "\n\n" + aide_recue("une organisation", quelle_orga)
		phrase_5 = "\n\n" + commanditaire_recompense("une organisation", quelle_orga)

	elif payeur == "un réseau" :
		quelle_orga = hasard(reseau)
		une_personne = commanditaire_personne("un réseau", quelle_orga)		
		phrase_2 = "un réseau " + quelle_orga +" en la personne de " + une_personne
		phrase_3 = choix_quete("un réseau", quelle_orga)
		phrase_4 = "\n\n" + aide_recue("un réseau", quelle_orga)
		phrase_5 = "\n\n" + commanditaire_recompense("un réseau", quelle_orga)

	else : #"une personne"
		phrase_2 = personne()
		phrase_3 = afficher_quete(hasard(quete))
		phrase_4 = "\n\nLes héros devront se débrouiller seuls."
		phrase_5 = "\n\n" + afficher_recompense()

	return phrase_1 + phrase_2 + "\n\n" + phrase_3 + phrase_4 + phrase_5

def commanditaire_personne(commanditaire, quelle_orga):
	genre = hasard(pers_genre)
	if genre == "féminin" :
		pronom = "elle"
		pronom_maj = "Elle"
	elif genre == "masculin" :
		pronom = "il"
		pronom_maj = "Il"
	else : # genre == "masculin" :
		pronom = "iel"
		pronom_maj = "Iel"

	race = hasard(pers_race)

	if commanditaire == "une organisation" :
		if quelle_orga == "le palais de justice" :
			metier = hasard(poste_palais_justice) + " au palais de justice"
		elif quelle_orga == "la caserne" :
			metier = hasard(poste_caserne) + " dans la caserne"
		elif quelle_orga == "La capitainerie" :
			metier = hasard(poste_capitainerie) + " dans la capitainerie"
		elif quelle_orga == "le chateau" :
			metier = hasard(poste_chateau) + " dans le chateau"
		elif quelle_orga == "le temple" :
			metier = hasard(poste_temple) + " dans le temple"
		else : # la guilde des voleurs, marchands, assassins, prostituées, médecins
			metier = hasard(poste_guilde) + " de " + quelle_orga
	else : #commanditaire == "un réseau"
		metier = hasard(poste_guilde) + " de ce réseau " + quelle_orga

	phrase_1 = nom_pers(genre, race) + "."
	phrase_2 = "\nC'est une personne " + hasard(pers_age) + " de genre " + genre + ", de la race des "+race+"."
	phrase_3 = "\n" + pronom_maj +" est " + metier + "."
	phrase_4 = "\n" + pronom_maj + " cache un secret à propos "+ secret_personne() + "."

	return phrase_1 + phrase_2 + phrase_3 + phrase_4

def aide_recue(commanditaire, quelle_orga) :
	aide = hasard(adjuvant)
	if aide == "personne" :
		phrase_1 = "\nLes héros auront l'appui de " + commanditaire_personne(commanditaire, quelle_orga)
	elif aide == "non" :
		phrase_1 = "\nLes héros devront se débrouiller seuls."
	else : #"matériel"
		phrase_1 = "\nLes héros se voient proposer une aide matérielle."
	return phrase_1

def commanditaire_recompense(commanditaire, quelle_orga) :
	prix = hasard(recompense)
	phrase_1 = "La récompense est : "
	if prix == "un titre" :
		if quelle_orga == "le chateau" :
			phrase_2 = prix +" et des terres d'une valeur " +hasard(valeur)+ "."
		else :
			return commanditaire_recompense(commanditaire, quelle_orga)
	elif prix == "un objet précieux" :
		phrase_2 = prix + " : " +objet_precieux()+"."
	elif prix == "le recrutement" or prix == "une autorisation d'accès" :
		if commanditaire == "une organisation" :
			phrase_2 = prix + " dans " +quelle_orga+"."
		else : # commanditaire == "un réseau"
			phrase_2 = prix + " dans le réseau " +quelle_orga+"."
	elif prix == "des terres" :
		if quelle_orga == "le chateau" :
			phrase_2 = prix + " " + "d'une valeur " +hasard(valeur)+ "."
		else :
			return commanditaire_recompense(commanditaire, quelle_orga)
	else : #"de l'argent" "de l'or" "des bijoux"
		phrase_2 = prix + " " + "d'une valeur " +hasard(valeur)+ "."
	return phrase_1+phrase_2

def choix_quete(commanditaire, quelle_orga) :
	if commanditaire == "une organisation" :
		if quelle_orga == "la guilde des voleurs" :
			phrase_1 = quete_prio("voler")
		elif quelle_orga == "la guilde des marchands" :
			phrase_1 = quete_prio("livrer")
		elif quelle_orga == "le palais de justice" :
			phrase_1 =  afficher_quete("enquêter")
		elif quelle_orga == "La guilde des assassins" :
			phrase_1 = quete_prio("tuer")
		elif quelle_orga == "la caserne" :
			phrase_1 = afficher_quete(hasard(quetes_caserne))
			
		elif quelle_orga == "la guilde des prostituées" :
			phrase_1 = quete_prio("kidnaper")
		elif quelle_orga == "La capitainerie" :
			phrase_1 = quete_prio("livrer")
		elif quelle_orga == "la guilde des médecins" :
			phrase_1 = quete_prio("empoisonner")
		elif quelle_orga == "le temple" :
			phrase_1 = quete_prio("fabriquer")
		else : # quelle_orga == "le chateau"
			phrase_1 = afficher_quete(hasard(quete))
	else : # "un réseau" :
		if quelle_orga == "de braconnage" :
			phrase_1 = quete_prio("capturer")
		elif quelle_orga == "de prostitution" :
			phrase_1 = quete_prio("kidnaper")
		elif quelle_orga == "d'esclavage" :
			phrase_1 = quete_prio("kidnaper")
		elif quelle_orga == "de trafic de drogue" :
			phrase_1 = quete_prio("intercepter")
		elif quelle_orga == "de chantage" :
			phrase_1 = quete_prio("voler")
		elif quelle_orga == "de résistance" :
			phrase_1 = quete_prio("détruire")
		else : # quelle_orga == "de contrebande"
			phrase_1 = quete_prio("livrer")


	return phrase_1

def quete_prio(prio) :
	number = randrange(1,3,1)
	if number == 1 :
		return afficher_quete(prio)
	else :
		return afficher_quete(hasard(quete))