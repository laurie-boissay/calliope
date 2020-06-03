#!/usr/bin/python3.8
#coding:u8

from random import randrange

from collection_de_mots.quetes import *
from collection_de_mots.zone import *
from collection_de_mots.personnes import *
from collection_de_mots.activites import *
from collection_de_mots.trucs import *

from generer.nom import *
from generation.generer_personne import *

"""
Le type de quête ;
Les détails de la quête :
	cible, lieux, objet, mobile...
"""



#_____enquete___________________________________________________________



def scene_crime() :
	"""
	Définit la scène du crime :
	un lieu discret, une maison, une organisation.
	"""
	scene = lieu_crime[randrange(len(lieu_crime))]
	if scene == "lieu discret" :
		phrase_1 = lieu_discret[randrange(len(lieu_discret))]+"."
	elif scene == "une maison" :
		phrase_1 = maison[randrange(len(maison))]+"."
	else : # "une organisation" :
		phrase_1 = "dans "+ organisation[randrange(len(organisation))]+"."
	return phrase_1

def enquete_kidnaping() :
	"""
	Détails pour résoudre l'enquête du kidnaping.
	- qui a été enlevé ;
	- ou cette personne est-elle retenue ;
	- qui est le coupable ;
	- quel est le mobile.
	"""
	phrase_2 = "Il s'agit de "+personne()
	scene = lieu_crime[randrange(len(lieu_crime))]
	if scene == "lieu discret" :
		phrase_3 = "\nCette personne est retenue "+lieu_discret[randrange(len(lieu_discret))]+"."
	elif scene == "une maison" :
		phrase_3 = "\nCette personne est retenue "+maison[randrange(len(maison))]+"."
	else : # "une organisation" :
		phrase_3 = "\nCette personne est retenue dans "+organisation[randrange(len(organisation))]+"."
	phrase_4 = "\n\nLe coupable est "+personne()
	phrase_5 = "\nLe mobile est "+mobile[randrange(len(mobile))]+"."
	return phrase_2+phrase_3+phrase_4+phrase_5

#_______________________________________________________________________________________________

def type_lieu_ville() :
	"""
	Génère un lieu en ville :
	maison de quelqu'un, une auberge, un navire, un autre type de bâtiment.
	"""
	type = batiment[randrange(len(batiment))]
	if type == "une maison":
		phrase_1 = "la maison de "+personne() + ".\nCette personne vit " + ou_en_ville()
	elif type == "la taverne":
		phrase_1 = "une taverne : "+nom_auberge() + " " + ou_en_ville()
	elif type == "un navire":
		phrase_1 = "un navire : "+nom_navire() + " " + ou_en_ville()
	else : # "le temple" "la mairie" "la serre royale" "l'orphelinat" "l'hôpital" "la prison"
		phrase_1 = type + " " + ou_en_ville()
	return phrase_1

def truc_a_voler() :
	"""
	Définit un nombre d'objets ou d'animaux et génère des détails sur l'endroit ou les trouver
	et la personne à qui ils appartiennent.
	"""
	truc = vol[randrange(len(vol))]
	if truc == "objet" :
		truc = objet[randrange(len(objet))]
		if truc ==  "uniforme(s)" :
			return str(randrange(1, 10, 1)) + " " + truc + " dans " + type_lieu_ville()
		else :
			return str(randrange(1, 10, 1)) + " " + truc + "."
	elif truc == "objet personnel" :
		return objet_pers[randrange(len(objet_pers))] + ". Chez " + personne() + "\nCette personne vit " + ou_en_ville()
	elif truc == "animal" :
		return animal_domestique[randrange(len(animal_domestique))]+" appartenant à "+personne() + "\nCette personne vit " + ou_en_ville()
	elif truc == "caisse" :
		return str(randrange(1 , 10, 1))+" caisse(s) "+caisse[randrange(len(caisse))]+" dans "+ type_lieu_ville()
	else : #argent
		return "de l'"+truc+" en "+quantite[randrange(len(quantite))]+"."


def qui_paye() :
	"""
	Définit un point de livraison.
	une organisation, un lieu discret, la maison de quelqu'un, une auberge.
	"""
	payeur = commanditaire[randrange(len(commanditaire))]
	if payeur == "une organisation" :
		return "\nLa livraison se fera dans "+organisation[randrange(len(organisation))]+". Ils seront attendus."
	elif payeur == "un réseau" :
		contact = lieu_discret[randrange(len(lieu_discret))]
		phrase_1 = "\nLa livraison est pour un réseau "+reseau[randrange(len(reseau))]+". Ils trouverons leur contact "+contact
		if contact == "dans la taverne" :
			return phrase_1+" : "+nom_auberge()+"."
		else :
			return phrase_1+"."
	else :
		return "\nLa livraison se fera chez "+personne()

def cible_protection() :
	"""
	Ce que les héros doivent protéger : 
	une personne, un secret, un objet personnel, un convoi, un lieu

	Beaucoup de détails si la cible est un convoi :
	type de convoi, date de départ, durée du trajet, destination du convoi.
	"""
	cible = protection[randrange(len(protection))]
	if cible == "une personne" :
		proteger = personne()
	elif cible == "un secret" :
		proteger = "le secret de "+personne()
	elif cible == "un objet personnel" :
		proteger = objet_pers[randrange(len(objet_pers))]+" appartenant à "+personne()
	elif cible == "un convoi" :
		phrase_1 = type_convoi()+".\nIl part dans "+str(randrange(1, 3, 1))+" jour(s) pour"
		phrase_2 = zone()
		phrase_3 = "\nLe voyage devrait durer "+str(randrange(1, 10, 1))+" jour(s)."
		proteger = phrase_1+" "+phrase_2+" "+phrase_3
	else : #"un lieu"
		proteger = type_lieu_ville()
	return proteger + " " + menace(cible)

def menace(cible_protection):
	"""
	Selon la cible à protéger, définit la menace qui pèse dessus.
	"""
	if cible_protection == "une personne" :
		raison = menace_personne[randrange(len(menace_personne))]
		menace = "Cette personne est menacée de " + raison + " par "+ entite()
	elif cible_protection == "un secret" :
		menace = "Ce secret risque d'être révélé par " + entite()
	elif cible_protection == "un objet personnel" :
		menace = "On peut craindre " + menace_objet_perso[randrange(len(menace_objet_perso))] + " de cet objet par " + entite()
	elif cible_protection == "un convoi" :
		menace = "Sur la route du convoi, les héros risquent de croiser " + creature[randrange(len(creature))] + "."
	else : #"un lieu"
		phrase_1 = "Grâce à un informateur, les héros savent que cet endroit va être la cible d'une attaque.\n"
		phrase_2 = "A la tête de cet assaut "+ entite() + "\n"
		phrase_3 = "\nLe but est " + menace_lieu[randrange(len(menace_lieu))] + " de la cible."
		menace = phrase_1 + phrase_2 + phrase_3
	return "\n\n" + menace

def entite():
	"""
	Génère une entité soit :
	une organisation, une personne, un réseau.
	"""
	qui = commanditaire[randrange(len(commanditaire))]
	if qui == "une organisation" :
		qui = organisation[randrange(len(organisation))]+"."
	elif qui == "une personne" :
		qui = personne()
	else : #"un réseau"
		qui = "un réseau " + reseau[randrange(len(reseau))]+"."
	return qui

def cible_livraison() :
	"""
	Génère ce que les héros doivent livrer.
	"""
	truc = livraison[randrange(len(livraison))]
	if truc == "une personne" :
		phrase_1 = personne() + "\n\nLa cible se cache "
	elif truc == "un objet" :
		truc = objet[randrange(len(objet))]
		phrase_1 = str(randrange(1, 10, 1))+" "+truc + " "
	elif truc == "un objet personnel" :
		phrase_1 = objet_pers[randrange(len(objet_pers))]+" "
	elif truc == "un animal" :
		phrase_1 = animal_domestique[randrange(len(animal_domestique))]+" "
	elif truc == "une caisse" :
		phrase_1 = str(randrange(1, 10, 1))+" caisse(s) "+caisse[randrange(len(caisse))]+" "
	else : # "de l'argent" "un animal"
		phrase_1 = truc+" en "+quantite[randrange(len(quantite))]+" "	

	return phrase_1 + ou_en_ville()

def type_animal() :
	"""
	Génère un type d'animal :
	un animal sauvage, un animal domestique, des animaux d'élevage.
	"""
	type = quel_animal[randrange(len(quel_animal))]
	if type == "animal sauvage" :
		return "un "+animal_sauvage[randrange(len(animal_sauvage))]+" sauvage"
	elif type == "animal domestique" :
		return animal_domestique[randrange(len(animal_domestique))]+" appartenant à "+personne()
	else :
		return "des "+animal_elevage[randrange(len(animal_elevage))]+"."

def type_convoi() :
	"""
	Définit ce que transporte le convoit.
	"""
	marchandises = convoi[randrange(len(convoi))]
	if marchandises == "de caisses" :
		return "un convoi de caisses "+caisse[randrange(len(caisse))]
	else :
		return "un convoi "+marchandises

def mission_infiltrer() :
	"""
	définit le but de la mission d'infiltration.
	"""
	phrase_1 = cible_infiltration()
	raison = raison_inf[randrange(len(raison_inf))]
	if raison == "voler" :
		phrase_2 = "\nIls pourront alors voler "+objet_pers[randrange(len(objet_pers))]+"."
	elif raison == "protéger" or raison == "libérer" or raison == "sauver" :
		phrase_2 = "\nIls pourront alors "+raison+" "+personne()
	elif raison == "tuer" :
		phrase_2 = "\nIls pourront alors tuer la personne à la tête de cette organisation.\nC'est "+personne()
	else : #"détruire"
		phrase_2 = "\nIls pourront alors détruire cette organisation de l'intérieur."
	return phrase_1 + phrase_2

def cible_infiltration() :
	"""
	Quel réseau ou quelle organisation les héros doivent infiltrer.
	"""
	inf = infiltration[randrange(len(infiltration))]
	if inf == "un réseau" :
		phrase_1 = "un réseau "+reseau[randrange(len(reseau))]+"."
	else : #"une organisation"
		phrase_1 = organisation[randrange(len(organisation))]+"."
	return phrase_1

def mission_kidnaper() :
	"""
	Qui ou qu'est-ce que les héros doivent kidnaper.
	"""
	cible = kid[randrange(len(kid))]
	if cible == "personne" :
		phrase_1 = personne()  + "\nLa cible réside " + ou_en_ville()
	else : #"animal"
		cible = animal_domestique[randrange(len(animal_domestique))]
		phrase_1 = cible + " appartenant à "+personne()
	return phrase_1

def mission_tuer() :
	"""
	Qui ou qu'est-ce que les héros doivent tuer et ou le trouver ou, 
	ou le livrer.
	"""
	cible = kill[randrange(len(kill))]	
	if cible == "personne" :
		phrase_1 = personne() + "\n\nLa cible vit " + ou_en_ville()
	elif cible == "monstre" :
		phrase_1 = creature[randrange(len(creature))] + " dans " + lieu_quete() + "." + ou_nature()
	elif cible == "animal sauvage" :
		phrase_1 = str(randrange(1, 10, 1))+" "+animal_sauvage[randrange(len(animal_sauvage))]+"."+qui_paye()
	else : #"animal"
		phrase_1 ="un animal.\nC'est "+animal_domestique[randrange(len(animal_domestique))]+" appartenant à "+personne()
	return phrase_1

def mission_detruire() :
	"""
	Ce que les héros doivent détruire et ou le trouver.
	"""
	cible = destruction[randrange(len(destruction))]
	if cible == "un objet" :
		phrase_1 = objet_pers[randrange(len(objet_pers))]+" appartenant à "+ personne() + "\n\nCette personne vit " + ou_en_ville()
	elif cible == "une organisation" :
		phrase_1 = organisation[randrange(len(organisation))]+" " + ou_en_ville()
	elif cible == "un réseau" :
		phrase_1 = cible+" "+reseau[randrange(len(reseau))]+".\nIls trouverons une de leurs câches " + lieu_discret[randrange(len(lieu_discret))]+ " " + ou_en_ville()
	else :#"un bâtiment"
		phrase_1 = type_lieu_ville()
	return phrase_1

def quel_monstre() :
	"""
	Génère un monstre (animal sacré ou créature) et l'endroit ou le trouver.
	"""
	cible = monstre[randrange(len(monstre))]
	if cible == "animal sacré" :
		phrase_1 = animal_sacre()
		phrase_2 = " dans "+lieu_quete_ext()
	else : #"créature"
		phrase_1 = creature[randrange(len(creature))]
		phrase_2 = " dans "+lieu_quete()
	return phrase_1+phrase_2

def mission_intercepter() :
	"""
	Ce que les héros doivent intercepter
	La date prévu de son arrivée dans la zone.
	"""
	cible = interception[randrange(len(interception))]
	phrase_2 = " qui vient de : " + zone()
	phrase_3 = " qui viennent de : " + zone()

	if cible == "un convoi" :
		phrase_1 = type_convoi()+ phrase_2 + "\n\nCe convoi doit arriver"
	elif cible == "des documents sensibles" :
		phrase_1 = cible + phrase_3 + "\n\nLe porteur est "+personne()+"\nSon arrivée est prévu"
	else : #"une lettre"
		phrase_1 = cible + phrase_2 + "\n\nLe porteur est "+personne()+"\nSon arrivée est prévu"
	return phrase_1 + " dans " + str(randrange(1, 3, 1))+ " jour(s)."

def mission_empoisonement() :
	"""
	Qui ou qu'est-ce que les héros doivent empoisonner.
	Ou le trouver.
	"""
	cible = poison[randrange(len(poison))]
	if cible == "un animal domestique" :
		phrase_1 = animal_domestique[randrange(len(animal_domestique))]+" appartenant à "+personne()+ "\nSa demeure se trouve " + ou_en_ville()
	elif cible ==  "une personne" :
		phrase_1 = personne() + "\nSa demeure se trouve " + ou_en_ville()
	elif cible ==  "des caisses de nourriture" :
		phrase_1 = cible + ". Elles sont dans " + type_lieu_ville()
	else : #  "le puit d'un village"
		phrase_1 = "le puit " + ou_en_ville()
	return phrase_1

def ou_en_ville() :
	"""
	Indique une direction cardinale et une distance (parfois en jours de marche)
	pour une zone en ville.
	"""
	point = quelle_zone[randrange(len(quelle_zone))]
	if point == "ici" :
		phrase_1 = "tout près d'ici, " +rose_vent[randrange(len(rose_vent))] + "."
	else : #"ailleurs"
		phrase_1 = "dans " + zone() + "\nIl faudra " +str(randrange(1, 10, 1))+ " jour(s) de marche aux héros pour s'y rendre."

	return phrase_1

def ou_nature() :
	"""
	Indique une direction cardinale et une distance (parfois en jours de marche)
	pour une zone dans la nature.
	"""
	phrase_2 = "\nIl faudra " +str(randrange(5, 10, 1))+ " jour(s) de marche aux héros pour s'y rendre."
	point = quelle_zone[randrange(len(quelle_zone))]
	if point == "ici" :
		phrase_1 = "\nC'est " +rose_vent[randrange(len(rose_vent))] + " d'ici."
	else : #"ailleurs"
		phrase_1 = "\nC'est " +rose_vent[randrange(len(rose_vent))] + " de : " + zone()

	return phrase_1 + phrase_2

def mission_fabriquer() :
	"""
	Définit les 3 étapes nécessaires pour résoudre une quête de type "fabriquer":
		- ou trouver les composants ;
		- ou fabriquer l'objet ;
		- quel monstre tuer avec cet objet et ou le trouver.
	"""
	phrase_1 = objet_precieux() + " :\n"
	phrase_2 = "\n1) Il leur faudra d'abord trouver les composants dans " + lieu_quete()+ "." + ou_nature()
	phrase_3 = "\n\n2) Puis ils se rendront dans " + lieu_quete()+ " pour fabriquer l'objet." + ou_nature()
	phrase_4 = "\n\n3) Leur quête prendra fin lorsqu'ils aurront tué " + quel_monstre() + " dans "+ lieu_quete_ext() + "." + ou_nature()

	return phrase_1 + phrase_2 + phrase_3 + phrase_4

