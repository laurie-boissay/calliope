from random import randrange

from generation.generer_quete import *

from collection_de_mots.quetes import *
#from collection_de_mots.zone import *
from collection_de_mots.personnes import *
from collection_de_mots.activites import *
#from collection_de_mots.trucs import *




	

"""




def afficher_recompense() :
	
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
	
	number = randrange(1,3,1)
	if number == 1 :
		return afficher_quete(prio)
	else :
		return afficher_quete(quete[randrange(len(quete))])

"""