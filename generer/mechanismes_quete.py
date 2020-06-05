#!/usr/bin/python3.8
#coding:u8

from random import randrange

from collection_de_mots.quetes import *
from collection_de_mots.zone import *
from collection_de_mots.personnes import *
from collection_de_mots.activites import *
from collection_de_mots.trucs import *

from generer.classe_personnage import Personnage
from generer.nom import *


"""
Les détails de la quête :
cible, lieux, objet, mobile...
"""


def gen_perso_def_metier(metier):
	"""
	Grâce à la classe Personnage,
	génère un personnage dont on a décidé du métier.

	Prend le paramètre metier en entrée.

	Renvoie un texte décrivant le personnage + 
	en italique, la commande permettant de générer
	le détail du personnage.
	"""
	perso = Personnage()
	perso.set_particularites()
	perso.set_metier(metier)
	personne = perso.pnj_light()
	return description(personne)


def poste_dans(structure):
	"""
	Prend en entrée un commanditaire. 
	("une personne", une organisation précise, un réseau précis)

	Renvoie le texte d'un nom de métier possible.
	"""
	if "la guilde" in structure:
		metier = poste_guilde[randrange(len(poste_guilde))] + " de " + structure
	
	elif structure == "le palais de justice":
		metier = poste_palais_justice[randrange(len(poste_palais_justice))] + " dans " + structure

	elif structure == "la caserne":
		metier = poste_caserne[randrange(len(poste_caserne))] + " dans " + structure

	elif structure == "la capitainerie":
		metier = poste_capitainerie[randrange(len(poste_capitainerie))] + " dans " + structure

	elif structure == "le chateau":
		metier = poste_chateau[randrange(len(poste_chateau))] + " dans " + structure

	elif structure == "le temple":
		metier = poste_temple[randrange(len(poste_temple))] + " dans " + structure

	elif structure == "une personne":
		metier = ""

	else: # réseau
		metier = poste_guilde[randrange(len(poste_guilde))] + " d'un réseau " + structure

	return metier


def genere_affiche_perso_light() :
	"""
	Génère un personnage.

	Renvoie un texte décrivant le personnage + 
	en italique, la commande permettant de générer
	le détail du personnage.
	"""
	perso = Personnage()

	perso.set_particularites()
	personne = perso.pnj_light()
	text = description(personne)
	return text


def victime_morte(victime):
	"""
	Renvoie un texte au passé décrivant un personnage décédé.
	"""
	text = ""

	text += "La victime était une personne " + victime["age"] + " de genre " + victime["genre"]
	text += ".\n" + victime["pronom"] + " s'appelait " + victime["prénom"] + " " + victime["nom"]
	text += ". " + victime["pronom"] + " était de la race des " + victime["race"] + "s.\n"
	text += victime["pronom"] + " exerçait le métier de " + victime["métier"] + ". "
	text += victime["prénom"] + " cachait un secret " + victime["secret"] + ".\n"
	
	return text


def description(personne):
	"""
	Renvoie un texte décrivant le personnage + 
	en italique, la commande permettant de générer
	le détail du personnage.
	"""	
	text = personne["prénom"] + " " + personne["nom"] + ". C'est une personne "
	text += personne["age"] + " de genre " + personne["genre"] 
	text += ", de la race des " + personne["race"] + "s. "
	text += personne["pronom"] + " est " + personne["métier"] + "."
	
	text += "\n\n*!pnj, 12, 3, prénom=" + personne['prénom'] + ", nom=" + personne['nom']
	text += ", métier=" + personne['métier'] + ", race=" + personne['race'] 
	text += ", genre=" + personne["genre"] + ", age=" + personne["age"] + "*" + "\n"

	return text
		

#_____enquete___________________________________________________________

def scene_crime() :
	"""
	Définit la scène du crime :
	un lieu discret, une maison, une organisation.

	Renvoie un texte.
	"""
	scene = lieu_crime[randrange(len(lieu_crime))]

	if scene == "lieu discret" :
		text = lieu_discret[randrange(len(lieu_discret))] + "."

	elif scene == "une maison" :
		text = maison[randrange(len(maison))] + "."

	else : # "une organisation" :
		text = "dans " + organisation[randrange(len(organisation))] + "."
			
	return text


def enquete_kidnaping(victime) :
	"""
	Détails pour résoudre l'enquête du kidnaping.
	- qui a été enlevé ;
	- ou cette personne est-elle retenue ;
	- qui est le coupable ;
	- quel est le mobile.

	Renvoie un texte.
	"""
	text = "Il s'agit de " + description(victime) + "\n"
	text += victime["pronom"] + " est retenu.e "
	scene = lieu_crime[randrange(len(lieu_crime))]

	if scene == "lieu discret" :
		text += lieu_discret[randrange(len(lieu_discret))] + "."
		text += "\n\nLe coupable est " + genere_affiche_perso_light()

	elif scene == "une maison" :
		text += maison[randrange(len(maison))] + "."
		text += "\n\nLe coupable est " + genere_affiche_perso_light()
	else : # "une organisation" :
		nom_organisation = organisation[randrange(len(organisation))]
		text += "dans " + nom_organisation + "."
		text += "\n\nLe coupable est " + genere_affiche_perso_light()
	
	text += "\nLe mobile est " + mobile[randrange(len(mobile))] + "."
	
	return text


#_______________________________________________________________________________________________

def qui_paye(personne, type_payeur, payeur) :
	"""
	Définit un point de livraison en fonction du commanditaire :
	une organisation, un lieu discret, la maison de quelqu'un, une auberge.

	Renvoie un texte.
	"""
	if type_payeur == "une organisation" :
		text = "\nLa livraison se fera dans " + payeur + ". Ils seront attendus."

	elif type_payeur == "un réseau" :
		contact = lieu_discret[randrange(len(lieu_discret))]
		text = "\nLa livraison est pour le réseau " + payeur
		text += ". Ils trouverons leur contact " + contact

		if contact == "dans la taverne" :
			text += " : " + nom_auberge() + "."
		else :
			text += "."
	else :
		text = "\nLa livraison se fera chez " + description(personne)

	return text


def truc_a_voler() :
	"""
	Définit un nombre d'objets ou d'animaux et génère des détails sur l'endroit ou les trouver
	et la personne à qui ils appartiennent.

	Renvoie un texte.
	"""
	truc = vol[randrange(len(vol))]

	if truc == "objet personnel" :
		text = objet_pers[randrange(len(objet_pers))] + ". Chez "
		text += genere_affiche_perso_light()
	
	elif truc == "caisse" :
		text = str(randrange(1 , 10, 1)) + " caisse(s) " + caisse[randrange(len(caisse))]
		text += " dans "+ type_lieu_ville()

	return text


def mission_fabriquer() :
	"""
	Définit les 3 étapes nécessaires pour résoudre une quête de type "fabriquer":
		- ou trouver les composants ;
		- ou fabriquer l'objet ;
		- quel monstre tuer avec cet objet et ou le trouver.

	Renvoie un texte.
	"""
	text = objet_precieux() + " :\n"
	
	text += "\n1) Il leur faudra d'abord trouver les composants dans " 
	text += lieu_quete()+ "." + ou_nature()
	
	text += "\n\n2) Puis ils se rendront dans " + lieu_quete()
	text += " pour fabriquer l'objet." + ou_nature()

	text += "\n\n3) Leur quête prendra fin lorsqu'ils aurront terrassé "
	text += quel_monstre() + " dans "+ lieu_quete_ext() + "." + ou_nature()

	return text


def mission_tuer() :
	"""
	Qui ou qu'est-ce que les héros doivent tuer et ou le trouver.

	Renvoie un texte.
	"""
	cible = kill[randrange(len(kill))]	
	
	if cible == "personne" :
		text = genere_affiche_perso_light() + "\n\nLa cible vit " + ou_en_ville()
	
	elif cible == "monstre" :
		text = creature[randrange(len(creature))] + " dans " + lieu_quete() + "." + ou_nature()
	
	elif cible == "animal sauvage" :
		text = str(randrange(1, 10, 1))+" "+animal_sauvage[randrange(len(animal_sauvage))] + "."
	
	else : #"animal"
		text ="un animal.\nC'est "+animal_domestique[randrange(len(animal_domestique))]
		text += " appartenant à "+genere_affiche_perso_light()

	return text


def type_lieu_ville() :
	"""
	Génère un lieu en ville :
	maison de quelqu'un, une auberge, un navire, un autre type de bâtiment.

	Renvoie un texte.
	"""
	type = batiment[randrange(len(batiment))]
	
	if type == "une maison":
		text = "la maison de " + genere_affiche_perso_light() + ".\nCette personne vit " + ou_en_ville()
	
	elif type == "la taverne":
		text = "une taverne : " + nom_auberge() + " " + ou_en_ville()
	
	elif type == "un navire":
		text = "un navire : " + nom_navire() + " " + ou_en_ville()
	
	else : # "le temple" "la mairie" "la serre royale" "l'orphelinat" "l'hôpital" "la prison"
		text = type + " " + ou_en_ville()
	
	return text


def cible_protection() :
	"""
	Ce que les héros doivent protéger : 
	une personne, un secret, un objet personnel, un convoi, un lieu.

	Beaucoup de détails si la cible est un convoi :
	type de convoi, date de départ, durée du trajet, destination du convoi.

	Renvoie un texte.
	"""
	cible = protection[randrange(len(protection))]

	if cible == "une personne" :
		proteger = genere_affiche_perso_light()
	
	elif cible == "un secret" :
		proteger = "le secret de "+ genere_affiche_perso_light()
	
	elif cible == "un objet personnel" :
		proteger = objet_pers[randrange(len(objet_pers))]+" appartenant à "+ genere_affiche_perso_light()
	
	elif cible == "un convoi" :
		proteger = type_convoi()+".\nIl part dans "+str(randrange(1, 3, 1))+" jour(s) pour"
		proteger += zone()
		proteger += "\nLe voyage devrait durer "+str(randrange(1, 10, 1))+" jour(s)."

	else : #"un lieu"
		proteger = type_lieu_ville()
	
	return proteger + " " + menace(cible)


def menace(cible_protection):
	"""
	Selon la cible à protéger, définit la menace qui pèse dessus.

	Renvoie un texte.
	"""
	if cible_protection == "une personne" :
		raison = menace_personne[randrange(len(menace_personne))]
		menace = "Cette personne est menacée de " + raison + " par "+ entite()
	
	elif cible_protection == "un secret" :
		menace = "Ce secret risque d'être révélé par " + entite()
	
	elif cible_protection == "un objet personnel" :
		menace = "On peut craindre " + menace_objet_perso[randrange(len(menace_objet_perso))]
		menace = " de cet objet par " + entite()

	elif cible_protection == "un convoi" :
		menace = "Sur la route du convoi, les héros risquent de croiser "
		menace = creature[randrange(len(creature))] + "."

	else : #"un lieu"
		menace = "Grâce à un informateur, les héros savent que cet endroit va être la cible d'une attaque.\n"
		menace += "A la tête de cet assaut "+ entite() + "\n"
		menace += "\nLe but est " + menace_lieu[randrange(len(menace_lieu))] + " de la cible."

	return menace


def entite():
	"""
	Génère une entité soit :
	une organisation, une personne, un réseau.

	Renvoie un texte.
	"""
	qui = commanditaire[randrange(len(commanditaire))]
	
	if qui == "une organisation" :
		qui = organisation[randrange(len(organisation))] + "."
	
	elif qui == "une personne" :
		qui = genere_affiche_perso_light()
	
	else : #"un réseau"
		qui = "un réseau " + reseau[randrange(len(reseau))] + "."
	
	return qui


def cible_livraison() :
	"""
	Génère ce que les héros doivent livrer.

	Renvoie un texte.
	"""
	truc = livraison[randrange(len(livraison))]
	
	if truc == "une personne" :
		text = genere_affiche_perso_light() + "\n\nLa cible se cache "
	
	elif truc == "un objet" :
		truc = objet[randrange(len(objet))]
		text = str(randrange(1, 10, 1)) + " " + truc + " "
	
	elif truc == "un objet personnel" :
		text = objet_pers[randrange(len(objet_pers))] + " "
	
	elif truc == "un animal" :
		text = animal_domestique[randrange(len(animal_domestique))] + " "
	
	elif truc == "une caisse" :
		text = str(randrange(1, 10, 1))+" caisse(s) "+caisse[randrange(len(caisse))] + " "
	
	else : # "de l'argent" "un animal"
		text = truc + " en " + quantite[randrange(len(quantite))] + " "	

	return text + ou_en_ville()


def type_animal() :
	"""
	Génère un type d'animal :
	un animal sauvage, un animal domestique, des animaux d'élevage.

	Renvoie un texte.
	"""
	type = quel_animal[randrange(len(quel_animal))]
	
	if type == "animal sauvage" :
		text = "un "+animal_sauvage[randrange(len(animal_sauvage))]+" sauvage"
	
	elif type == "animal domestique" :
		text = animal_domestique[randrange(len(animal_domestique))]+" appartenant à "
		text += genere_affiche_perso_light()
	
	else :
		text = "des "+animal_elevage[randrange(len(animal_elevage))]+"."

	return text


def type_convoi() :
	"""
	Définit ce que transporte le convoit.

	Renvoie un texte.
	"""
	marchandises = convoi[randrange(len(convoi))]
	
	if marchandises == "de caisses" :
		return "un convoi de caisses " + caisse[randrange(len(caisse))]
	
	else :
		return "un convoi " + marchandises


def mission_infiltrer() :
	"""
	Définit le but de la mission d'infiltration.

	Renvoie un texte.
	"""
	text, cible = cible_infiltration()
	raison = raison_inf[randrange(len(raison_inf))]
	
	if raison == "voler" :
		text += "\nIls pourront alors voler " + objet_pers[randrange(len(objet_pers))] + "."
	
	elif raison == "protéger" or raison == "libérer" or raison == "sauver" :
		text += "\nIls pourront alors " + raison + " " + genere_affiche_perso_light()
	
	elif raison == "tuer" :
		metier = poste_dans(cible)
		text += "\nIls pourront alors tuer " + gen_perso_def_metier(metier)
	
	else : #"détruire"
		text += "\nIls pourront alors détruire cette organisation de l'intérieur."
	
	return text


def cible_infiltration() :
	"""
	Quel réseau ou quelle organisation les héros doivent infiltrer.

	Renvoie deux textes.
	"""
	inf = infiltration[randrange(len(infiltration))]
	
	if inf == "un réseau" :
		cible = reseau[randrange(len(reseau))]
		text = "un réseau " + cible + "."
	
	else : #"une organisation"
		cible = organisation[randrange(len(organisation))]
		text = cible + "."
	
	return text, cible


def mission_kidnaper() :
	"""
	Qui ou qu'est-ce que les héros doivent kidnaper.

	Renvoie un texte.
	"""
	cible = kid[randrange(len(kid))]
	
	if cible == "personne" :
		text = genere_affiche_perso_light()  + "\nLa cible réside " + ou_en_ville()
	
	else : #"animal"
		cible = animal_domestique[randrange(len(animal_domestique))]
		text = cible + " appartenant à "+genere_affiche_perso_light()
	
	return text


def mission_detruire() :
	"""
	Ce que les héros doivent détruire et ou le trouver.

	Renvoie un texte.
	"""
	cible = destruction[randrange(len(destruction))]
	
	if cible == "un objet" :
		text = objet_pers[randrange(len(objet_pers))] + " appartenant à "
		text += genere_affiche_perso_light() + "\n\nCette personne vit " + ou_en_ville()

	elif cible == "une organisation" :
		text = organisation[randrange(len(organisation))]+" " + ou_en_ville()
	
	elif cible == "un réseau" :
		text = cible+" "+reseau[randrange(len(reseau))] + ".\nIls trouverons une de leurs câches "
		text += lieu_discret[randrange(len(lieu_discret))] + " " + ou_en_ville()

	else :#"un bâtiment"
		text = type_lieu_ville()
	
	return text


def quel_monstre() :
	"""
	Génère un monstre (animal sacré ou créature) et l'endroit ou le trouver.

	Renvoie un texte.
	"""
	cible = monstre[randrange(len(monstre))]
	
	if cible == "animal sacré" :
		text = animal_sacre()
		text += " dans "+lieu_quete_ext()
	
	else : #"créature"
		text = creature[randrange(len(creature))]
		text += " dans "+lieu_quete()
	
	return text


def mission_intercepter() :
	"""
	Ce que les héros doivent intercepter
	La date prévu de son arrivée dans la zone.

	Renvoie un texte.
	"""
	cible = interception[randrange(len(interception))]
	
	if cible == "un convoi" :
		texte = type_convoi() + " qui vient de : " + zone() + "\n\nCe convoi doit arriver dans "
	
	elif cible == "des documents sensibles" :
		texte = cible + " qui viennent de : " + zone() + "\n\nLe porteur est "
		texte += genere_affiche_perso_light() + "\nSon arrivée est prévu dans "

	else : #"une lettre"
		texte = cible + " qui vient de : " + zone() + "\n\nLe porteur est "
		texte += genere_affiche_perso_light()+"\nSon arrivée est prévue dans "
		
	return texte + str(randrange(1, 3, 1)) + " jour(s)."


def mission_empoisonnement() :
	"""
	Qui ou qu'est-ce que les héros doivent empoisonner.
	Ou le trouver.

	Renvoie un texte.
	"""
	cible = poison[randrange(len(poison))]
	
	if cible == "un animal domestique" :
		text = animal_domestique[randrange(len(animal_domestique))] + " appartenant à "
		text += genere_affiche_perso_light() + "\nSa demeure se trouve " + ou_en_ville()

	elif cible ==  "une personne" :
		text = genere_affiche_perso_light() + "\nSa demeure se trouve " + ou_en_ville()
	
	elif cible ==  "des caisses de nourriture" :
		text = cible + ". Elles sont dans " + type_lieu_ville()
	
	else : #  "le puit d'un village"
		text = "le puit " + ou_en_ville()
	
	return text


def ou_en_ville() :
	"""
	Indique une direction cardinale et une distance (parfois en jours de marche)
	pour une zone en ville.

	Renvoie un texte.
	"""
	point = quelle_zone[randrange(len(quelle_zone))]
	
	if point == "ici" :
		texte = "tout près d'ici, " +rose_vent[randrange(len(rose_vent))] + "."
	
	else : #"ailleurs"
		texte = "dans " + zone() + "\nIl faudra " +str(randrange(1, 10, 1))
		texte += " jour(s) de marche aux héros pour s'y rendre."

	return texte


def ou_nature() :
	"""
	Indique une direction cardinale et une distance (parfois en jours de marche)
	pour une zone dans la nature.

	Renvoie un texte.
	"""
	
	point = quelle_zone[randrange(len(quelle_zone))]
	
	if point == "ici" :
		texte = "\nC'est " + rose_vent[randrange(len(rose_vent))] + " d'ici."
	
	else : #"ailleurs"
		texte = "\nC'est " + rose_vent[randrange(len(rose_vent))] + " de : " + zone()

	texte += "\nIl faudra " + str(randrange(5, 10, 1)) + " jour(s) de marche aux héros pour s'y rendre."
	
	return texte
