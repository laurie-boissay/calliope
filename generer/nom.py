from random import randrange


from collection_de_mots.quetes import *
from collection_de_mots.zone import *
from collection_de_mots.personnes import *
from collection_de_mots.activites import *
from collection_de_mots.trucs import *

"""
Génère des noms de lieux, d'objets, d'animaux, de personnes, de métier.
	
Décrit une zone de type ville ou village.
"""


def nom_auberge() :
	"""
	Pioche un nom + un ajectif pour former un nom d'auberge.
	"""
	return auberge_nom[randrange(len(auberge_nom))] + " " + auberge_adj[randrange(len(auberge_adj))]

def nom_navire() :
	"""
	Pioche un nom + un ajectif pour former un nom de navire.
	"""
	return navire_nom[randrange(len(navire_nom))] + " " + navire_adj[randrange(len(navire_adj))]

def objet_precieux() :
	"""
	Pioche un nom + un ajectif pour former un nom d'objet précieux.
	"""
	return objet_nom[randrange(len(objet_nom))] + " " + objet_adj[randrange(len(objet_adj))]

def lieu_quete() :
	"""
	Pioche un nom + un ajectif pour former un lieu de quête couvert.
	"""
	return lieu_quete_nom[randrange(len(lieu_quete_nom))] + " " + lieu_quete_adj[randrange(len(lieu_quete_adj))]

def lieu_quete_ext() :
	"""
	Pioche un nom + un ajectif pour former un lieu de quête en extérieur.
	"""
	return ext_nom[randrange(len(ext_nom))] + " " + ext_adj[randrange(len(ext_adj))]

def animal_sacre():
	"""
	Pioche un nom + un ajectif pour former un nom d'animal sacré.
	"""
	return "le/l' "+ animal_sauvage[randrange(len(animal_sauvage))] + " " + objet_adj[randrange(len(objet_adj))]

def zone() :
	"""
	Cette fonction permet de créer le descriptif d'une zone.
		- nom de la zone ;
		- taille de la zone ;
		- densité de la population ;
		- races les plus reprsentées ;
		- activités principales ;
		- la richesse des habitants ;
		- climat ;
		- détails sur le paysage.
	"""
	activite_1 = activite[randrange(len(activite))]
	activite_2 = activite[randrange(len(activite))]
	taille = superficie[randrange(len(superficie))]
	rich = richesse[randrange(len(richesse))]
	temp = climat[randrange(len(climat))]
	pop = quantite_pop[randrange(len(quantite_pop))]


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
		phrase_4 = "La population est "+rich+". Le climat est "+temp+". La zone est "+paysage[randrange(len(paysage))]+"."
		return  phrase_0+"\n\n"+phrase_1 + phrase_2 +"\n"+ phrase_3 +"\n"+ phrase_4


def nom_pers(genre, race) :
	"""
	Donne un nom et un prénom au personnage selon :
		- son genre ;
		- sa race.

	Particularité pour les demi-orcs qui ont soit un couple prénom-nom humain ou orc.
	Le choix est aléatoire.

	Autre particularité pour le genre androgyne ou autre genre définit par l'utilisateur,
	un genre pour le nom est pioché aléatoirement et la fonction boucle sur elle même.

	Enfin, quand l'utilisateur à définit une autre race que celle listée dans pers_race,
	une race est piochée pour son nom de personnage.
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
		elif race == "halfelins" or race =="halfelin":
			nom = prenoms_halfelins_f[randrange(len(prenoms_halfelins_f))] + " " + noms_halfelins[randrange(len(noms_halfelins))]
		elif race == "gnomes" or race =="gnome":
			nom = prenoms_gnomes_f[randrange(len(prenoms_gnomes_f))] + " " +noms_gnomes[randrange(len(noms_gnomes))]
		elif race == "demi-orcs" or race == "demi-orc":
			race = race_nom[randrange(len(race_nom))]
			if race == "orcs" or race == "orc":
				nom = prenoms_orcs_f[randrange(len(prenoms_orcs_f))] + " du-clan-de-" + prenoms_orcs_f[randrange(len(prenoms_orcs_f))]
			else : #nom et prénom humain
				nom = prenoms_humains_f[randrange(len(prenoms_humains_f))] + " " + noms_humains[randrange(len(noms_humains))]
		else : # Autres races
			race = pers_race[randrange(len(pers_race))]
			return nom_pers(genre, race)

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
		elif race == "halfelins" or race == "halfelin":
			nom = prenoms_halfelins_m[randrange(len(prenoms_halfelins_m))] + " " + noms_halfelins[randrange(len(noms_halfelins))]
		elif race == "gnomes" or race =="gnome":
			nom = prenoms_gnomes_f[randrange(len(prenoms_gnomes_f))] + " " +noms_gnomes[randrange(len(noms_gnomes))]
		elif race == "demi-orcs" or race == "demi-orc":
			race = race_nom[randrange(len(race_nom))]
			if race == "orcs" or race == "orc":
				nom = prenoms_orcs_m[randrange(len(prenoms_orcs_m))] + " du-clan-de-" + prenoms_orcs_m[randrange(len(prenoms_orcs_m))]
			else : #nom et prénom humain
				nom = prenoms_humains_m[randrange(len(prenoms_humains_m))] + " " + noms_humains[randrange(len(noms_humains))]
		else : # Autres races
			race = pers_race[randrange(len(pers_race))]
			return nom_pers(genre, race)

	else : # autres genres
		genre = genre_nom[randrange(len(genre_nom))]
		return nom_pers(genre, race)
	return nom


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
	"""
	Définit la spécialité des apprenti.e.s en piochant dans la liste des métiers.

	Certaines associations apprenti/e-métier sont proscrites comme : apprenti/e apprenti/e.
	La fonction vérifie la spécialité piochée avec la liste pas_apprenti_e.

	En cas de concordance, la fonction boucle sur elle même.
	"""
	metier = pers_metier[randrange(len(pers_metier))]
	if metier in pas_apprenti_e:
		return specialite()
	else:
		return metier


def habitants():
	"""
	Pioche deux races d'habitants.
	"""
	race_1 = pers_race[randrange(len(pers_race))]
	race_2 = pers_race[randrange(len(pers_race))]
	if race_1 == race_2 :
		return habitants()
	else :
		return " Habitée mojoritairement par des "+race_1+". Il y a aussi quelques "+race_2+"."

def nom_zone(taille, rich, pop, activite_1):
	"""
	Génère un nom de zone selon :
		- la taille de la zone ;
		- La densité de population de la zone ;
		- la richesse des habitants ;
		- l'activité pricipale.
	"""
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
		phrase_4 = commercants[randrange(len(commercants))]
	elif activite_1 == "l'esclavage" :
		phrase_4 = esclavage[randrange(len(esclavage))]
	elif activite_1 == "la religion" :
		phrase_4 = religion[randrange(len(religion))]
	elif activite_1 == "la magie" :
		phrase_4 = magie[randrange(len(magie))]
	elif activite_1 == "la contrebande" :
		phrase_4 = "franc/he"
	elif activite_1 == "l'élevage" :
		phrase_4 = eleveurs[randrange(len(eleveurs))]
	elif activite_1 == "l'alcool" :
		phrase_4 = alcool[randrange(len(alcool))]
	elif activite_1 == "la drogue" :
		phrase_4 = drogue[randrange(len(drogue))]
	elif activite_1 == "la pêche" :
		phrase_4 = "des pêcheurs"
	elif activite_1 == "la chasse" :
		phrase_4 = chasse[randrange(len(chasse))]
	elif activite_1 == "l'agriculture" :
		phrase_4 = "des champs verts"
	elif activite_1 == "l'artisanat" :
		phrase_4 = artisants[randrange(len(artisants))]
	else : #activite_1 == "extraction minière" :
		phrase_4 = matiere_extraite[randrange(len(matiere_extraite))]
	return phrase_1 + phrase_2 + phrase_3 + phrase_4


