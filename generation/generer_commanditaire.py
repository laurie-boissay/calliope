from random import randrange

from generation.generer_quete import *

from collection_de_mots.quetes import *
from collection_de_mots.zone import *
from collection_de_mots.personnes import *
from collection_de_mots.activites import *
from collection_de_mots.trucs import *

"""
Definit la structure des quêtes :
	- le point de départ : le commanditaire ;
	- le type de quete ;
	- l'aide fournie aux PJ ;
	- la récompense proposée.
"""


def generer_commanditaire() :
	"""
	Le commanditaire peut etre une personne, une organisation, un réseau.
	le choix se fait grâce à randrange en piochant dans une collection de mots.

	Cette fonction appelle les fonctions :
		- commanditaire_personne ;
		- personne ;
		- choix_quete ;
		- aide_recue ;
		- commanditaire_recompense ;
		- afficher_recompense.
	"""
	payeur = commanditaire[randrange(len(commanditaire))]
	phrase_1 = "\nLes héros sont approchés par "

	if payeur == "une organisation" :
		quelle_orga = organisation[randrange(len(organisation))]
		une_personne = commanditaire_personne("une organisation", quelle_orga)		
		phrase_2 = quelle_orga + " en la personne de " + une_personne
		phrase_3 = choix_quete("une organisation", quelle_orga)
		phrase_4 = "\n\n" + aide_recue("une organisation", quelle_orga)
		phrase_5 = "\n\n" + commanditaire_recompense("une organisation", quelle_orga)

	elif payeur == "un réseau" :
		quelle_orga = reseau[randrange(len(reseau))]
		une_personne = commanditaire_personne("un réseau", quelle_orga)		
		phrase_2 = "un réseau " + quelle_orga +" en la personne de " + une_personne
		phrase_3 = choix_quete("un réseau", quelle_orga)
		phrase_4 = "\n\n" + aide_recue("un réseau", quelle_orga)
		phrase_5 = "\n\n" + commanditaire_recompense("un réseau", quelle_orga)

	else : #"une personne"
		phrase_2 = personne()
		phrase_3 = afficher_quete(quete[randrange(len(quete))])
		phrase_4 = "\n\nLes héros devront se débrouiller seuls."
		phrase_5 = "\n\n" + afficher_recompense()

	return phrase_1 + phrase_2 + "\n\n" + phrase_3 + phrase_4 + phrase_5

def aide_recue(commanditaire, quelle_orga) :
	"""
	Définit quel type d'aide les héros peuvent attendre pour réussir leur quête : 
	aucune, aide matérielle, appui d'une autre personne.
	"""
	aide = adjuvant[randrange(len(adjuvant))]
	if aide == "personne" :
		phrase_1 = "\nLes héros auront l'appui de " + commanditaire_personne(commanditaire, quelle_orga)
	elif aide == "non" :
		phrase_1 = "\nLes héros devront se débrouiller seuls."
	else : #"matériel"
		phrase_1 = "\nLes héros se voient proposer une aide matérielle."
	return phrase_1

def commanditaire_recompense(commanditaire, quelle_orga) :
	"""
	Définit une récompense lorsque le commanditaire est une organisation ou un réseau.

	Selon le type de commanditaire, la récompense va varier :

	Tous les commanditaires peuvent offir un objet précieux 
	(nom + adj piochés dans une collection de mots.), de l'argent,
	de l'or, des bijoux.

	Une organisation ou un réseau peuvent offir un recrutement ou
	une autorisation d'accés.

	Le chateau peut offir, en plus des autres types de récompenses,
	des terres ou un titre.
	
	"""
	prix = recompense[randrange(len(recompense))]
	phrase_1 = "La récompense est : "
	if prix == "un titre" :
		if quelle_orga == "le chateau" :
			phrase_2 = prix +" et des terres d'une valeur " + valeur[randrange(len(valeur))]+ "."
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
			phrase_2 = prix + " " + "d'une valeur " + valeur[randrange(len(valeur))]+ "."
		else :
			return commanditaire_recompense(commanditaire, quelle_orga)
	else : #"de l'argent" "de l'or" "des bijoux"
		phrase_2 = prix + " " + "d'une valeur " + valeur[randrange(len(valeur))]+ "."
	return phrase_1+phrase_2

def afficher_recompense() :
	"""
	Définit une récompense lorsque le commanditaire est une personne.
	Un "particulier" peut offrir en récompense :
		de l'argent, de l'or, des bijoux ou un objet précieux.
	"""
	prix = recompense[randrange(len(recompense))]
	phrase_1 = "La récompense est : "
	if prix == "un titre" or prix == "le recrutement" or prix == "une autorisation d'accès" or prix == "des terres" :
		return afficher_recompense()
	elif prix == "un objet précieux" :
		phrase_2 = prix + " : " +objet_precieux()+"."
	else : #"de l'argent" "de l'or" "des bijoux"
		phrase_2 = prix + " " + "d'une valeur " +valeur[randrange(len(valeur))]+ "."
	return phrase_1+phrase_2

def choix_quete(commanditaire, quelle_orga) :
	"""
	Les commanditaires de type organisation et réseau vont proposer des
	quêtes selon leur(s) priorité(s).
	"""
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
			phrase_1 = afficher_quete(quetes_caserne[randrange(len(quetes_caserne))])
			
		elif quelle_orga == "la guilde des prostituées" :
			phrase_1 = quete_prio("kidnaper")
		elif quelle_orga == "La capitainerie" :
			phrase_1 = quete_prio("livrer")
		elif quelle_orga == "la guilde des médecins" :
			phrase_1 = quete_prio("empoisonner")
		elif quelle_orga == "le temple" :
			phrase_1 = quete_prio("fabriquer")
		else : # quelle_orga == "le chateau"
			phrase_1 = afficher_quete(quete[randrange(len(quete))])
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
	"""
	La quête définie prioritaire a (un peu plus d') 1 chance sur 3 d'être piochée.
	Le reste du temps, la quête sera piochée dans la totalité de la liste de quêtes.
	"""
	number = randrange(1,3,1)
	if number == 1 :
		return afficher_quete(prio)
	else :
		return afficher_quete(quete[randrange(len(quete))])

