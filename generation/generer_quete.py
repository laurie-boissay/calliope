#!/usr/bin/python3.8
#coding:u8

from random import randrange

from menu import *

from collection_de_mots.quetes import *
from collection_de_mots.zone import *
from collection_de_mots.personnes import *
from collection_de_mots.activites import *
from collection_de_mots.trucs import *

from generation.generer_nom import *

def afficher_quete(mission):
	phrase_1 = "Les héros devront "
	if mission == "voler" :
		return phrase_1 + "__**voler**__ "+ truc_a_voler()+qui_paye()

	elif mission == "infiltrer" :
		return phrase_1 + "__**infiltrer**__ "+mission_infiltrer()
	
	elif mission == "protéger" :
		return phrase_1 + "__**protéger**__ "+ cible_protection()
	
	elif mission == "livrer" :
		return phrase_1 + "__**livrer**__ "+ cible_livraison()+qui_paye()
	
	elif mission == "enquêter" :
		return phrase_1 + "__**enquêter**__ sur " +  mission_enqueter()
	
	elif mission == "kidnaper" :
		return phrase_1 + "__**kidnaper**__ "+ mission_kidnaper() + "\n" + qui_paye()

	elif mission == "tuer" :
		return phrase_1 + "__**tuer**__ "+ mission_tuer()

	elif mission == "détruire" :
		return phrase_1 + "__**détruire**__ "+ mission_detruire()

	elif mission == "trouver" :
		return phrase_1 + "__**trouver**__ "+ objet_precieux()+" dans "+lieu_quete()+"." +ou_nature()

	elif mission == "sauver" :
		return phrase_1 + "__**sauver**__ "+ personne()+"\nLes héros trouverons cette personne dans "+type_lieu_ville() + menace("une personne")

	elif mission == "fabriquer" :
		return phrase_1 + "__**fabriquer**__ " + mission_fabriquer()

	elif mission == "capturer" :
		return phrase_1 + "__**capturer**__ " + animal_sacre() +" dans "+ lieu_quete_ext()+ "." + ou_nature() + "\n" + qui_paye()

	elif mission == "empoisonner" :
		return phrase_1 + "__**empoisonner**__ " + mission_empoisonement()

	else : #"intercepter"
		return phrase_1 + "__**intercepter**__ " + mission_intercepter()

def afficher_recompense() :
	prix = hasard(recompense)
	phrase_1 = "La récompense est : "
	if prix == "un titre" or prix == "le recrutement" or prix == "une autorisation d'accès" or prix == "des terres" :
		return afficher_recompense()
	elif prix == "un objet précieux" :
		phrase_2 = prix + " : " +objet_precieux()+"."
	else : #"de l'argent" "de l'or" "des bijoux"
		phrase_2 = prix + " " + "d'une valeur " +hasard(valeur)+ "."
	return phrase_1+phrase_2

#_____personne_________________________________________________________

def personne():
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
	metier =  metier_pers()

	phrase_1 = nom_pers(genre, race) + "."
	phrase_2 = "\nC'est une personne " + hasard(pers_age) + " de genre " + genre + ", de la race des "+race+"."
	phrase_3 = "\n" + pronom_maj +" est " + metier + "."
	phrase_4 = "\n" + pronom_maj + " cache un secret à propos "+ secret_personne() + "."

	return phrase_1 + phrase_2 + phrase_3 + phrase_4

def nom_pers(genre, race) :
	if genre == "féminin" :
		if race == "humains" :
			nom = hasard(prenoms_humains_f) + " " + hasard(noms_humains)
		elif race == "nains" :
			nom = hasard(prenoms_nains_f) + " " + hasard(noms_nains)
		elif race == "elfes" :
			nom = hasard(prenoms_elfes_f) + " " + hasard(noms_elfes)
		elif race == "orcs" :
			nom = hasard(prenoms_orcs_f) + " du clan de " + hasard(prenoms_orcs_f)
		elif race == "demi-elfes" :
			nom = hasard(prenoms_elfes_f) + " " + hasard(noms_humains)
		elif race == "demi-orcs" :
			race = hasard(race_nom)
			if race == "orc" :
				nom = hasard(prenoms_orcs_f) + " du clan de " + hasard(prenoms_orcs_f)
			else : #humain
				nom = hasard(prenoms_humains_f) + " " + hasard(noms_humains)
		elif race == "halfelins" :
			nom = hasard(prenoms_halfelins_f) + " " + hasard(noms_halfelins)
		else : # "gnomes"
			nom = hasard(prenoms_gnomes_f) + " " + hasard(noms_gnomes)
	elif genre == "masculin" :
		if race == "humains" :
			nom = hasard(prenoms_humains_m) + " " + hasard(noms_humains) 
		elif race == "nains" :
			nom = hasard(prenoms_nains_m) +" "+ hasard(noms_nains)
		elif race == "elfes" :
			nom = hasard(prenoms_elfes_m) + " " + hasard(noms_elfes)
		elif race == "orcs" :
			nom = hasard(prenoms_orcs_m) + " du clan de " + hasard(prenoms_orcs_m)
		elif race == "demi-elfes" :
			nom = hasard(prenoms_elfes_m) + " " + hasard(noms_humains)
		elif race == "demi-orcs" :
			race = hasard(race_nom)
			if race == "orc" :
				nom = hasard(prenoms_orcs_m) + " du clan de " + hasard(prenoms_orcs_m)
			else : #humain
				nom = hasard(prenoms_humains_m) + " " + hasard(noms_humains)
		elif race == "halfelins" :
			nom = hasard(prenoms_halfelins_m) + " " + hasard(noms_halfelins)
		else : # "gnomes"
			nom = hasard(prenoms_gnomes_m) + " " + hasard(noms_gnomes)
	else : #"andorgyne"
		genre = hasard(genre_nom)
		return nom_pers(genre, race)
	return nom

def secret_personne() :
	secret = hasard(pers_secret)
	return secret

def indiscret() :
	return "Quelqu'un dont le métier est "+metier_pers()+" est au courrant de son secret."

def metier_pers() :
	metier = hasard(pers_metier)
	if metier == "haut placé/e" :
		phrase_1 = metier + " dans " +hasard(organisation)
	elif metier == "éleveur/éleveuse" :
		phrase_1 = metier + " de/d' " + hasard(animal_elevage)
	elif metier == "paysan/ne" :
		phrase_1 = metier + " dans la culture " + hasard(champ)
	elif metier == "servante/serviteur" :
		phrase_1 = metier+ " dans " + hasard(organisation)
	elif metier == "serveur/serveuse" or metier == "tavernier/e" :
		phrase_1 = metier + " dans l'auberge " + nom_auberge()
	elif metier == "marchand/e" :
		phrase_1 = metier + " de/d' " + hasard(commerce)
	elif metier == "capitaine" :
		phrase_1 = metier + " du bateau " + nom_navire()
	elif metier == "artisan/ne" :
		phrase_1 = metier + " " + hasard(artisanat)
	else :
		phrase_1 = metier
	return phrase_1

#_____enquete___________________________________________________________

def mission_enqueter():
	raison = hasard(enquete)
	phrase_1 = raison +" :\n\n"	
	if raison == "un meurtre" :
		phrase_2 = "La victime est "+personne()+"\n\nLe mobile est "+hasard(mobile)+".\n\n"+hasard(description)+".\n\n"+"Le corps a été retrouvé "+scene_crime()+"\n\nLe coupable est "+personne()	
	elif raison == "un kidnaping" :
		phrase_2 = enquete_kidnaping()
	elif raison == "une organisation" :
		phrase_2 = "C'est "+hasard(organisation)+".\nLes héros doivent démasquer un espion.\nC'est "+personne()
	elif raison == "une personne" :
		phrase_2 = "Il s'agit d'"+personne()
	elif raison == "un vol" :
		phrase_2 = "Il s'agit d'"+ truc_a_voler() +"\n\nLe coupable est "+personne()
	else : #"un réseau"
		phrase_2 = "C'est un réseau "+hasard(reseau)+".\nLes héros doivent identifier le chef du réseau.\nC'est "+personne()
	return phrase_1 + phrase_2

def scene_crime() :
	scene = hasard(lieu_crime)
	if scene == "lieu discret" :
		phrase_1 = hasard(lieu_discret)+"."
	elif scene == "une maison" :
		phrase_1 = hasard(maison)+"."
	else : # "une organisation" :
		phrase_1 = "dans "+ hasard(organisation)+"."
	return phrase_1

def enquete_kidnaping() :
	phrase_2 = "Il s'agit d'"+personne()
	scene = hasard(lieu_crime)
	if scene == "lieu discret" :
		phrase_3 = "\nElle est retenue "+hasard(lieu_discret)+"."
	elif scene == "une maison" :
		phrase_3 = "\nElle est retenue "+hasard(maison)+"."
	else : # "une organisation" :
		phrase_3 = "\nElle est retenue dans "+hasard(organisation)+"."
	phrase_4 = "\n\nLe coupable est "+personne()
	phrase_5 = "\nLe mobile est "+hasard(mobile)+"."
	return phrase_2+phrase_3+phrase_4+phrase_5

#________lieux_________________________________________________________


def type_lieu_ville() :
	type = hasard(batiment)
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
	truc = hasard(vol)
	if truc == "objet" :
		truc = hasard(objet)
		if truc ==  "uniforme(s)" :
			return str(randrange(1, 10, 1)) + " " + truc + " dans " + type_lieu_ville()
		else :
			return str(randrange(1, 10, 1)) + " " + truc + "."
	elif truc == "objet personnel" :
		return hasard(objet_pers) + ". Chez " + personne() + "\nCette personne vit " + ou_en_ville()
	elif truc == "animal" :
		return hasard(animal_domestique)+" appartenant à "+personne() + "\nCette personne vit " + ou_en_ville()
	elif truc == "caisse" :
		return str(randrange(1 , 10, 1))+" caisse(s) "+hasard(caisse)+" dans "+ type_lieu_ville()
	else : #argent
		return "de l'"+truc+" en "+hasard(quantite)+"."

def qui_paye() :
	payeur = hasard(commanditaire)
	if payeur == "une organisation" :
		return "\nLa livraison se fera dans "+hasard(organisation)+". Ils seront attendus."
	elif payeur == "un réseau" :
		contact = hasard(lieu_discret)
		phrase_1 = "\nLa livraison est pour un réseau "+hasard(reseau)+". Ils trouverons leur contact "+contact
		if contact == "dans la taverne" :
			return phrase_1+" : "+nom_auberge()+"."
		else :
			return phrase_1+"."
	else :
		return "\nLa livraison se fera chez "+personne()
	
def generer_contact() :
	contact = hasard(lieu_discret)
	if contact == "dans la taverne" :
			return phrase_1+" : "+nom_auberge()+"."
	else :
		""" 
		"dans la forêt""dans les égouts""dans une grotte"
		"dans les docs""dans la montagne""dans la taverne""sur les berges de la rivière"
		"""
		return phrase_1+"."

def cible_protection() :
	cible = hasard(protection)
	if cible == "une personne" :
		proteger = personne()
	elif cible == "un secret" :
		proteger = "le secret de "+personne()
	elif cible == "un objet personnel" :
		proteger = hasard(objet_pers)+" appartenant à "+personne()
	elif cible == "un convoi" :
		phrase_1 = type_convoi()+".\nIl part dans "+str(randrange(1, 3, 1))+" jour(s) pour"
		phrase_2 = zone()
		phrase_3 = "\nLe voyage devrait durer "+str(randrange(1, 10, 1))+" jour(s)."
		proteger = phrase_1+" "+phrase_2+" "+phrase_3
	else : #"un lieu"
		proteger = type_lieu_ville()
	return proteger + " " + menace(cible)

def menace(cible_protection):
	if cible_protection == "une personne" :
		raison = hasard(menace_personne)
		menace = "Cette personne est menacée de " + raison + " par "+ entite()
	elif cible_protection == "un secret" :
		menace = "Ce secret risque d'être révélé par " + entite()
	elif cible_protection == "un objet personnel" :
		menace = "On peut craindre " + hasard(menace_objet_perso) + " de cet objet par " + entite()
	elif cible_protection == "un convoi" :
		menace = "Sur la route du convoi, les héros risquent de croiser " + hasard(creature) + "."
	else : #"un lieu"
		phrase_1 = "Grâce à un informateur, les héros savent que cet endroit va être la cible d'une attaque.\n"
		phrase_2 = "A la tête de cet assaut "+ entite() + "\n"
		phrase_3 = "\nLe but est " + hasard(menace_lieu) + " de la cible."
		menace = phrase_1 + phrase_2 + phrase_3
	return "\n\n" + menace

def entite():
	qui = hasard(commanditaire)
	if qui == "une organisation" :
		qui = hasard(organisation)+"."
	elif qui == "une personne" :
		qui = personne()
	else : #"un réseau"
		qui = "un réseau " + hasard(reseau)+"."
	return qui

def cible_livraison() :
	truc = hasard(livraison)
	if truc == "une personne" :
		phrase_1 = personne() + "\n\nLa cible se cache "
	elif truc == "un objet" :
		truc = hasard(objet)
		phrase_1 = str(randrange(1, 10, 1))+" "+truc + " "
	elif truc == "un objet personnel" :
		phrase_1 = hasard(objet_pers)+" "
	elif truc == "un animal" :
		phrase_1 = hasard(animal_domestique)+" "
	elif truc == "une caisse" :
		phrase_1 = str(randrange(1, 10, 1))+" caisse(s) "+hasard(caisse)+" "
	else : # "de l'argent" "un animal"
		phrase_1 = truc+" en "+hasard(quantite)+" "	

	return phrase_1 + ou_en_ville()

def type_animal() :
	type = hasard(quel_animal)
	if type == "animal sauvage" :
		return "un "+hasard(animal_sauvage)+" sauvage"
	elif type == "animal domestique" :
		return hasard(animal_domestique)+" appartenant à "+personne()
	else :
		return "des "+hasard(animal_elevage)+"."

def type_convoi() :
	marchandises = hasard(convoi)
	if marchandises == "de caisses" :
		return "un convoi de caisses "+hasard(caisse)
	else :
		return "un convoi "+marchandises

def mission_infiltrer() :
	phrase_1 = cible_infiltration()
	raison = hasard(raison_inf)
	if raison == "voler" :
		phrase_2 = "\nIls pourront alors voler "+hasard(objet_pers)+"."
	elif raison == "protéger" or raison == "libérer" or raison == "sauver" :
		phrase_2 = "\nIls pourront alors "+raison+" "+personne()
	elif raison == "tuer" :
		phrase_2 = "\nIls pourront alors tuer la personne à la tête de cette organisation.\nC'est "+personne()
	else : #"détruire"
		phrase_2 = "\nIls pourront alors détruire cette organisation de l'intérieur."
	return phrase_1 + phrase_2

def cible_infiltration() :
	inf = hasard(infiltration)
	if inf == "un réseau" :
		phrase_1 = "un réseau "+hasard(reseau)+"."
	else : #"une organisation"
		phrase_1 = hasard(organisation)+"."
	return phrase_1

def mission_kidnaper() :
	cible = hasard(kid)
	if cible == "personne" :
		phrase_1 = personne()  + "\nLa cible réside " + ou_en_ville()
	else : #"animal"
		cible = hasard(animal_domestique)
		phrase_1 = cible + " appartenant à "+personne()
	return phrase_1

def mission_tuer() :
	cible = hasard(kill)	
	if cible == "personne" :
		phrase_1 = personne() + "\n\nLa cible vit " + ou_en_ville()
	elif cible == "monstre" :
		phrase_1 = hasard(creature) + " dans " + lieu_quete() + "." + ou_nature()
	elif cible == "animal sauvage" :
		phrase_1 = str(randrange(1, 10, 1))+" "+hasard(animal_sauvage)+"."+qui_paye()
	else : #"animal"
		phrase_1 ="un animal.\nC'est "+hasard(animal_domestique)+" appartenant à "+personne()
	return phrase_1

def mission_detruire() :
	cible = hasard(destruction)
	if cible == "un objet" :
		phrase_1 = hasard(objet_pers)+" appartenant à "+ personne() + "\n\nCette personne vit " + ou_en_ville()
	elif cible == "une organisation" :
		phrase_1 = hasard(organisation)+" " + ou_en_ville()
	elif cible == "un réseau" :
		phrase_1 = cible+" "+hasard(reseau)+".\nIls trouverons une de leurs câches " + hasard(lieu_discret)+ " " + ou_en_ville()
	else :#"un bâtiment"
		phrase_1 = type_lieu_ville()
	return phrase_1

def quel_monstre() :
	cible = hasard(monstre)
	if cible == "animal sacré" :
		phrase_1 = animal_sacre()
		phrase_2 = " dans "+lieu_quete_ext()
	else : #"créature"
		phrase_1 = hasard(creature)
		phrase_2 = " dans "+lieu_quete()
	return phrase_1+phrase_2

def mission_intercepter() :
	cible = hasard(interception)
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
	cible = hasard(poison)
	if cible == "un animal domestique" :
		phrase_1 = hasard(animal_domestique)+" appartenant à "+personne()+ "\nSa demeure se trouve " + ou_en_ville()
	elif cible ==  "une personne" :
		phrase_1 = personne() + "\nSa demeure se trouve " + ou_en_ville()
	elif cible ==  "des caisses de nourriture" :
		phrase_1 = cible + ". Elles sont dans " + type_lieu_ville()
	else : #  "le puit d'un village"
		phrase_1 = "le puit " + ou_en_ville()
	return phrase_1

def ou_en_ville() :
	point = hasard(quelle_zone)
	if point == "ici" :
		phrase_1 = "tout près d'ici, " + hasard(rose_vent) + "."
	else : #"ailleurs"
		phrase_1 = "dans " + zone() + "\nIl faudra " +str(randrange(1, 10, 1))+ " jour(s) de marche aux héros pour s'y rendre."

	return phrase_1

def ou_nature() :
	phrase_2 = "\nIl faudra " +str(randrange(5, 10, 1))+ " jour(s) de marche aux héros pour s'y rendre."
	point = hasard(quelle_zone)
	if point == "ici" :
		phrase_1 = "\nC'est " + hasard(rose_vent) + " d'ici."
	else : #"ailleurs"
		phrase_1 = "\nC'est " + hasard(rose_vent) + " de : " + zone()

	return phrase_1 + phrase_2

def mission_fabriquer() :
	phrase_1 = objet_precieux() + " :\n"
	phrase_2 = "\n1) Il leur faudra d'abord trouver les composants dans " + lieu_quete()+ "." + ou_nature()
	phrase_3 = "\n\n2) Puis ils se rendront dans " + lieu_quete()+ " pour fabriquer l'objet." + ou_nature()
	phrase_4 = "\n\n3) Leur quête prendra fin lorsqu'ils aurront tué " + quel_monstre() + " dans "+ lieu_quete_ext() + "." + ou_nature()

	return phrase_1 + phrase_2 + phrase_3 + phrase_4