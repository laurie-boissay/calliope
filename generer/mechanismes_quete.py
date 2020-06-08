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
	texte = description(personne)
	return texte

def genere_affiche_pj_light() :
	"""
	Génère un personnage.

	Renvoie un texte décrivant le personnage + 
	en italique, la commande permettant de générer
	le détail du personnage.
	"""
	perso = Personnage()

	perso.set_type_de_personnage_pj()
	perso.set_particularites()
	personne = perso.pnj_light()
	texte = description_pj(personne)
	return texte


def victime_morte(victime):
	"""
	Renvoie un texte au passé décrivant un personnage décédé.
	"""
	texte = ""

	texte += "La victime était une personne " + victime["age"] + " de genre " + victime["genre"]
	texte += ".\n" + victime["pronom"] + " s'appelait " + victime["prénom"] + " " + victime["nom"]
	texte += ". " + victime["pronom"] + " était de la race des " + victime["race"] + "s.\n"
	texte += victime["pronom"] + " exerçait le métier de " + victime["métier"] + ". "
	texte += victime["prénom"] + " cachait un secret " + victime["secret"] + ".\n"
	
	return texte


def description(personne):
	"""
	Renvoie un texte décrivant le personnage + 
	en italique, la commande permettant de générer
	le détail du personnage.
	"""	
	texte = personne["prénom"] + " " + personne["nom"] + ". C'est une personne "
	texte += personne["age"] + " de genre " + personne["genre"] 
	texte += ", de la race des " + personne["race"] + "s. "
	texte += personne["pronom"] + " est " + personne["métier"] + "."
	
	texte += "\n\n\*\*\*  *Fiche complète avec cette commande :*  \*\*\*"
	texte += "\n\n> *!pnj, 12, 3, prénom=" + personne['prénom'] + ", nom=" + personne['nom']
	texte += " , métier=" + personne['métier'] + ", race=" + personne['race'] 
	texte += " , genre=" + personne["genre"] + ", age=" + personne["age"] + "*" + "\n"

	return texte


def description_pj(pj):
	"""
	Renvoie un texte décrivant le personnage + 
	en italique, la commande permettant de générer
	le détail du personnage.
	"""	
	texte = pj["prénom"] + " " + pj["nom"] + " est une personne "
	texte += pj["age"] + " de genre " + pj["genre"] 
	texte += ", de la race des " + pj["race"] + "s. "
	texte += pj["pronom"] + " est " + pj["métier"] + ".\n"
	texte += commande_pj(pj)

	return texte


def commande_pj(pj):
	"""
	Renvoie la commande permettant de générer
	le détail du personnage.
	"""
	texte = "\n\n\*\*\*  *Fiche complète avec cette commande :*  \*\*\*"
	texte += "\n\n> !pj, 12, 3, prénom=" + pj['prénom'] + ", nom="
	texte += pj['nom'] + ", métier=" + pj['métier']
	texte += ", race=" + pj['race'] + ", genre="
	texte += pj["genre"] + ", secret=" + pj["secret"]
	texte += ", age=" + pj["age"]
	
	return texte


def commande_quete(type_quete):
	"""
	Renvoie le texte de la commande permettant de générer une quête de même type
	ainsi que la commande pour qfficher tous les types de quêtes.
	"""
	texte = "\*\*\*  *Génerez une autre quête du même type :*  \*\*\*"
	texte += "\n```!quête=" + type_quete + "```"

	texte += "\n\*\*\*  *Voir tous les types de quêtes :*  \*\*\*"
	texte += "\n```!+quêtes```"
	
	return texte


def recompense_de_quete(pnj_commanditaire, commanditaire, pnj_aide):
	"""
	Génère une récompense en fonction du pnj_commanditaire.

	Renvoie sa valeur à recompense.
	"""
	metier = pnj_commanditaire["métier"].split(" ")
	recompense = "avec de l'argent."
	
	if pnj_aide != {}:
		metier_2 = pnj_aide["métier"].split(" ")

		if metier_2[0] == "reine/roi" or metier_2[0] == "ministre" or metier_2[0] == "conseiller/e":
			recompense_quete.append("avec un titre.")
			recompense_quete.append("avec des terres.")
			recompense = recompense_quete[randrange(len(recompense_quete))]
			recompense_quete.remove("avec un titre.")
			recompense_quete.remove("avec des terres.")

	if metier[0] == "reine/roi" or metier[0] == "ministre" or metier[0] == "conseiller/e":
		recompense_quete.append("avec un titre.")
		recompense_quete.append("avec des terres.")
		recompense = recompense_quete[randrange(len(recompense_quete))]
		recompense_quete.remove("avec un titre.")
		recompense_quete.remove("avec des terres.")

	elif metier[0] == "servante/serviteur":
		lieu = list(pnj_commanditaire["métier"].split("dans "))
		recompense = "avec une autorisation d'accès officieuse dans " + lieu[1] + "."

	elif metier[0] == "haut-placé/e":
		lieu = list(pnj_commanditaire["métier"].split("dans "))
		recompense = "en les recrutant dans " + lieu[1] + "."

	elif "chef" in metier:	
		recompense = "en les recrutant."

	elif metier[0] == "marchand/e":
		marchandises = list(pnj_commanditaire["métier"].split(" de/d' "))
		recompense = "avec quelques " + marchandises[1]+ "."

	elif commanditaire == "la caserne":
		recompense_quete.append("avec un entraînement à manier l'arme de leur choix.")
		recompense = recompense_quete[randrange(len(recompense_quete))]
		recompense_quete.remove("avec un entraînement à manier l'arme de leur choix.")

	elif metier[0] == "capitaine" and commanditaire != "la capitainerie":
		commerce.remove("informations")
		marchandises = commerce[randrange(len(commerce))]
		commerce.append("informations")	
		recompense = "avec quelques " + marchandises + " de sa cargaison."

	elif metier[0] == "artisan/ne" or metier[0] == "astrologue" or metier[0] == "alchimiste":
		recompense = "en mettant ses talents d'" + pnj_commanditaire["métier"] + " à leur service."

	elif metier[0] == "forgeron/ne" or metier[0] == "cartographe" or metier[0] == "sorcier/sorcière":
		recompense = "en mettant ses talents de " + pnj_commanditaire["métier"] + " à leur service."

	elif metier[0] == "marin":
		recompense_quete.append("avec une carte marquée d'un X rouge.")
		recompense = recompense_quete[randrange(len(recompense_quete))]
		recompense_quete.remove("avec une carte marquée d'un X rouge.")

	elif metier[0] == "apprenti/e" or metier[0] == "mendiant/e":
		recompense = "en se mettant à leur service."
		recompense += commande_pj(pnj_commanditaire)

	elif metier[0] == "tavernier/e":
		auberge = list(pnj_commanditaire["métier"].split("dans "))
		recompense_quete.append("en leur offrant un tarif préféreciel dans " + auberge[1] + ".")
		recompense = recompense_quete[randrange(len(recompense_quete))]
		recompense_quete.remove("en leur offrant un tarif préféreciel dans " + auberge[1] + ".")

	elif metier[0] == "médecin" or commanditaire == "la guilde des médecins":
		recompense_quete.append("en leur offrant un tarif préféreciel sur tous les soins.")
		recompense = recompense_quete[randrange(len(recompense_quete))]
		recompense_quete.remove("en leur offrant un tarif préféreciel sur tous les soins.")

	elif commanditaire == "la guilde des marchands":
		recompense_quete.append("en leur offrant un tarif préféreciel dans toutes les boutiques de la ville.")
		recompense = recompense_quete[randrange(len(recompense_quete))]
		recompense_quete.remove("en leur offrant un tarif préféreciel dans toutes les boutiques de la ville.")

	elif commanditaire == "la guilde des prostituées":
		recompense_quete.append("en leur offrant un tarif préféreciel dans toutes les maisons closes de la ville.")
		recompense = recompense_quete[randrange(len(recompense_quete))]
		recompense_quete.remove("en leur offrant un tarif préféreciel dans toutes les maisons closes de la ville.")

	elif metier[0] == "prêtre/sse" or commanditaire == "le temple":
		recompense_quete.append("avec un objet magique : " + objet_precieux() + ".")
		recompense = recompense_quete[randrange(len(recompense_quete))]
		del recompense_quete[1]

	elif commanditaire == "la guilde des assassins":
		recompense_quete.append("en leur garantissant la protection de la guilde.")
		recompense = recompense_quete[randrange(len(recompense_quete))]
		recompense_quete.remove("en leur garantissant la protection de la guilde.")

	elif commanditaire == "la guilde des voleurs":
		recompense_quete.append("en leur garantissant la protection de la guilde.")
		recompense_quete.append("avec des bijoux.")
		recompense = recompense_quete[randrange(len(recompense_quete))]
		recompense_quete.remove("en leur garantissant la protection de la guilde.")
		recompense_quete.remove("avec des bijoux.")

	elif "drogue" in metier:
		recompense_quete.append("avec quelques échantillons de leur marchandise récréative.")
		recompense = recompense_quete[randrange(len(recompense_quete))]
		recompense_quete.remove("avec quelques échantillons de leur marchandise récréative.")

	return recompense


def contexte_rencontre_commanditaire(type_quete, type_commanditaire, commanditaire):
	"""
	Pioche le contexte de la quête en fonction du type de quête et du commanditaire.

	Renvoie un texte.
	"""
	contexte = ""

	if commanditaire == "une personne":
		commanditaire = "la taverne"

	if commanditaire == "le temple":
		contexte_quetes_legales.remove("tavernier")
		contexte_realiste = contexte_quetes_legales[randrange(len(contexte_quetes_legales))]
		contexte_quetes_legales.append("tavernier")
		contexte += phrases_contexte(contexte_realiste, commanditaire)

	elif (commanditaire == "la caserne" or commanditaire == "le chateau") and type_quete == "tuer":
		contexte += phrases_contexte("prime", commanditaire)
	
	elif commanditaire in la_ligue_de_l_ombre or type_quete in quetes_illegales:
		contexte_realiste = contexte_quetes_illegales[randrange(len(contexte_quetes_illegales))]
		contexte += phrases_contexte(contexte_realiste, commanditaire)
	
	else :
		contexte_realiste = contexte_quetes_legales[randrange(len(contexte_quetes_legales))]
		contexte += phrases_contexte(contexte_realiste, commanditaire)
		
	return contexte


def phrases_contexte(contexte_pioche, commanditaire):
	"""
	Renvoie le texte du contexte de quête.
	"""	
	# quêtes illégales
	if contexte_pioche == "Pst":
		texte = '"Pst, pst !"\nDans une ruelle sombre, une personne encapuchonnée essaie '
		texte += "d'attirer l'attention des héros.\n\nC'est "

	elif contexte_pioche == "personne ivre":
		texte = "Une personne visiblement ivre bouscule les héros, "
		texte +="s'excuse en rotant bruyament et repart en titubant.\n"
		texte += "Plus tard, un des héros retrouve dans une de ses poches "
		texte += "une note griffonnée lui indiquant de se rendre "
		texte += lieu_discret[randrange(len(lieu_discret))] + " à midi."
		texte += "\n\nLes héros pourront y rencontrer "

	elif contexte_pioche == "lettre":
		texte = "Une lettre a été glissée pendant la nuit, sous la porte de chambre des héros.\n"
		texte += "Il sont invités à se rendre ce soir à l'auberge : " + nom_auberge() + "."
		texte += "\n\nLes héros pourront y rencontrer "

	elif contexte_pioche == "garçon":
		texte = "Un enfant cours vers le groupe de héros, il est tout sourire.\n"
		texte += '"La personne là-bas" dit-il en montrant une silhouette en train de disparaître.\n'
		texte += '"Elle a dit de vous donner ça."\n'
		texte += "Il tend une lettre à personne la plus charismatique du groupe et attend quelques minutes...\n"
		texte += '"Elle a dit aussi que vous allez me donner une pièce parce-que vous êtes des hérOs !"\n\n'
		texte += "La lettre contient le message suivant : \n\"Rendez-vous ce soir à la taverne : "
		texte +=  nom_auberge() + ", demandez des bières rousses.\""
		texte += "\n\nLes héros rencontreront alors "

	elif contexte_pioche == "fille":
		texte = "Une enfant cours vers le groupe de héros, elle tribuche quelques-fois.\n"
		texte += '"La personne là-bas" dit-elle en montrant une silhouette vague appuyée contre un mur.\n'
		texte += '"Elle a dit que vous devez la suivre parce-que elle a du t\'avail pour vous."\n'
		texte += "La silhouette se redresse lentement, épouste ses vêtements et s'en va."
		texte += "\n\nAprès une filature plutôt facile, les héros rencontrent "

	elif contexte_pioche == "mendiant.e":
		texte = '"M\'sieurs Dames, une p\'tite pièce contre une info ?"\n'
		texte += '"Y\'a quelqu\'un la d\'dans qui cherche des types d\'vot\' genre pour un p\'tit boulot."'
		texte += "\n\nLe mendiant désigne une porte dérobée et leur décrit "

	elif contexte_pioche == "contact":
		texte = "Un contact informe les héros d'une opportinitée : "
		texte += '"Un travail bien payé, dans vos cordes mais j\'peux pas trop en dire plus."\n'
		texte += '"Si ça vous interresse, je vous mets en contact."'
		texte += "\n\nIl les mène jusqu'à l'auberge " + nom_auberge() + " et leur présente "

	# Quêtes légales
	elif contexte_pioche == "annonce":
		nom_taverne = nom_auberge()
		texte = "Devant la taverne : " + nom_taverne + ", sur un grand tableau en bois, "
		texte += "les héros remarquent une annonce :\n"
		texte += "\"Recrute mercenaires pour une mission urgente. Présentez-vous dans " + commanditaire
		texte += ".\"\n\nEn s'y rendant, les héros pourront rencontrer "

	elif contexte_pioche == "accostés":
		texte = "Les héros sont accostés dans la rue par "

	elif contexte_pioche == "tavernier":
		texte = "Alors que les héros sont à la taverne, le tavernier s'approche et leur dit : "
		texte += '"Y\'a quelqu\'un à cette table là-bas qui cherche à recruter un groupe gaillard'
		texte += ' un peu dans l\'genre du votre."'
		texte += "\n\nLes héros peuvent s'approcher de "

	elif contexte_pioche == "prime":
		texte = "Dans toute la ville des affiches sont placardées :\n\"" + commanditaire.capitalize()
		texte += " recrute des chasseurs de primes. Présentez-vous le matin.\"\n\n"
		texte += "Les héros pourront demander à voir "
		
	return texte

#_____enquete___________________________________________________________

def scene_crime() :
	"""
	Définit la scène du crime :
	un lieu discret, une maison, une organisation.

	Renvoie un texte.
	"""
	scene = lieu_crime[randrange(len(lieu_crime))]

	if scene == "lieu discret" :
		texte = lieu_discret[randrange(len(lieu_discret))] + "."

	elif scene == "une maison" :
		texte = "à son domicile."

	else : # "une organisation" :
		texte = "dans " + organisation[randrange(len(organisation))] + "."
			
	return texte


def enquete_kidnaping(victime) :
	"""
	Détails pour résoudre l'enquête du kidnaping.
	- qui a été enlevé ;
	- ou cette personne est-elle retenue ;
	- qui est le coupable ;
	- quel est le mobile.

	Renvoie un texte.
	"""
	texte = "Il s'agit de " + description(victime) + "\n"
	texte += victime["pronom"] + " est retenu.e "
	scene = lieu_crime[randrange(len(lieu_crime))]

	if scene == "lieu discret" :
		texte += lieu_discret[randrange(len(lieu_discret))] + "."
		texte += "\n\nLe coupable est " + genere_affiche_perso_light()

	elif scene == "une maison" :
		texte += maison[randrange(len(maison))] + "."
		texte += "\n\nLe coupable est " + genere_affiche_perso_light()
	else : # "une organisation" :
		nom_organisation = organisation[randrange(len(organisation))]
		texte += "dans " + nom_organisation + "."
		texte += "\n\nLe coupable est " + genere_affiche_perso_light()
	
	texte += "\nLe mobile est " + mobile[randrange(len(mobile))] + "."
	
	return texte

#_______________________________________________________________________________________________

def qui_paye(personne, type_payeur, payeur) :
	"""
	Définit un point de livraison en fonction du commanditaire :
	une organisation, un lieu discret, la maison de quelqu'un, une auberge.

	Renvoie un texte.
	"""
	if type_payeur == "une organisation" :
		texte = "\nLa livraison se fera dans " + payeur + ". Ils seront attendus."

	elif type_payeur == "un réseau" :
		contact = lieu_discret[randrange(len(lieu_discret))]
		texte = "Ils trouverons leur contact " + contact

		if contact == "dans la taverne" :
			texte += " : " + nom_auberge() + "."
		else :
			texte += "."
	else :
		texte = "\nLa livraison se fera chez " + description(personne)

	return texte


def truc_a_voler() :
	"""
	Définit un nombre d'objets et génère des détails sur l'endroit ou les trouver
	et la personne à qui ils appartiennent.

	Renvoie un texte.
	"""
	truc = vol[randrange(len(vol))]

	if truc == "objet personnel" :
		texte = objet_pers[randrange(len(objet_pers))] + " appartenant à "
		texte += genere_affiche_perso_light()
	
	elif truc == "caisse" :
		texte = str(randrange(1 , 10, 1)) + " caisse(s) " + caisse[randrange(len(caisse))]
		texte += " dans "+ type_lieu_ville()

	return texte


def truc_derobe():
	"""
	Définit un nombre d'objets et génère des détails sur l'endroit ou les trouver.

	Renvoie un texte.
	"""
	truc = vol[randrange(len(vol))]

	if truc == "objet personnel" :
		texte = objet_pers[randrange(len(objet_pers))] + "."

	elif truc == "caisse" :
		texte = str(randrange(1 , 10, 1)) + " caisse(s) " + caisse[randrange(len(caisse))]
		texte += " dans "+ type_lieu_ville()

	return texte


def mission_fabriquer() :
	"""
	Définit les 3 étapes nécessaires pour résoudre une quête de type "fabriquer":
		- ou trouver les composants ;
		- ou fabriquer l'objet ;
		- quel monstre tuer avec cet objet et ou le trouver.

	Renvoie un texte.
	"""
	texte = objet_precieux() + " :\n"
	
	texte += "\n1) Il leur faudra d'abord trouver les composants dans " 
	texte += lieu_quete()+ "." + ou_nature()
	
	texte += "\n\n2) Puis ils se rendront dans " + lieu_quete()
	texte += " pour fabriquer l'objet." + ou_nature()

	texte += "\n\n3) Leur quête prendra fin lorsqu'ils aurront terrassé "
	texte += quel_monstre() + " dans "+ lieu_quete_ext() + "." + ou_nature()

	return texte


def mission_tuer() :
	"""
	Qui ou qu'est-ce que les héros doivent tuer et ou le trouver.

	Renvoie un texte.
	"""
	cible = kill[randrange(len(kill))]	
	
	if cible == "personne" :
		texte = genere_affiche_perso_light() + "\n\nLa cible vit " + ou_en_ville()
	
	elif cible == "monstre" :
		texte = creature[randrange(len(creature))] + " dans " + lieu_quete() + "." + ou_nature()
	
	elif cible == "animal" :
		texte = str(randrange(1, 10, 1)) + " " + animal_sauvage[randrange(len(animal_sauvage))] + "."

	return texte


def type_lieu_ville() :
	"""
	Génère un lieu en ville :
	maison de quelqu'un, une auberge, un navire, un autre type de bâtiment.

	Renvoie un texte.
	"""
	type = batiment[randrange(len(batiment))]
	
	if type == "une maison":
		texte = "la maison de " + genere_affiche_perso_light() + ".\nCette personne vit " + ou_en_ville()
	
	elif type == "la taverne":
		texte = "une taverne : " + nom_auberge() + " " + ou_en_ville()
	
	elif type == "un navire":
		texte = "un navire : " + nom_navire() + " " + ou_en_ville()
	
	else : # "le temple" "la mairie" "la serre royale" "l'orphelinat" "l'hôpital" "la prison"
		texte = type + " " + ou_en_ville()
	
	return texte


def cible_protection(personne) :
	"""
	Ce que les héros doivent protéger : 
	une personne, un secret, un objet personnel, un convoi, un lieu.

	Beaucoup de détails si la cible est un convoi :
	type de convoi, date de départ, durée du trajet, destination du convoi.

	Renvoie un texte.
	"""
	cible = protection[randrange(len(protection))]

	if cible == "une personne" :
		proteger = personne
	
	elif cible == "un secret" :
		proteger = "le secret de " + personne
	
	elif cible == "un objet personnel" :
		proteger = objet_pers[randrange(len(objet_pers))] + "."

	elif cible == "un convoi" :
		proteger = type_convoi() + ".\nIl part dans " + str(randrange(1, 3, 1)) + " jour(s) pour "
		proteger += zone()
		proteger += "\nLe voyage devrait durer " + str(randrange(1, 10, 1)) + " jour(s)."

	else : #"un lieu"
		proteger = type_lieu_ville()
	
	prenom = personne.split(" ")
	proteger += "\n" + menace(prenom[0], cible)
	
	return proteger


def menace(prenom, cible):
	"""
	Selon la cible à protéger, définit la menace qui pèse dessus.

	Renvoie un texte.
	"""
	if cible == "une personne" :
		raison = menace_personne[randrange(len(menace_personne))]
		menace = "L'info vient d'une source sûre : "
		menace += prenom + " est menacé.e de " + raison + " par "+ entite()
	
	elif cible == "un secret" :
		menace = "Ce secret risque d'être révélé par " + entite()
	
	elif cible == "un objet personnel" :
		menace = "On peut craindre que cet objet soit volé par " + entite()

	elif cible == "un convoi" :
		menace = "Sur la route, le convoi risque de croiser "
		menace += creature[randrange(len(creature))] + "."

	else : #"un lieu"
		menace = "L'info vient d'une source sûre : cet endroit va être la cible d'une attaque.\n"
		menace += "A la tête de cet assaut "+ entite() + "\n"
		menace += "\nLe but de cette attaque est " + menace_lieu[randrange(len(menace_lieu))] + " de la cible."

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
		texte = genere_affiche_perso_light() + "\n\nLa cible se cache "
	
	elif truc == "un objet" :
		truc = objet[randrange(len(objet))]
		texte = str(randrange(1, 10, 1)) + " " + truc + " "
	
	elif truc == "un objet personnel" :
		texte = objet_pers[randrange(len(objet_pers))] + " "
	
	elif truc == "un animal" :
		texte = animal_domestique[randrange(len(animal_domestique))] + " "
	
	elif truc == "une caisse" :
		texte = str(randrange(1, 10, 1))+" caisse(s) "+caisse[randrange(len(caisse))] + " "
	
	else : # "de l'argent"
		texte = truc + " en " + quantite[randrange(len(quantite))] + " "	

	return texte + ou_en_ville()


def type_animal() :
	"""
	Génère un type d'animal :
	un animal sauvage, un animal domestique, des animaux d'élevage.

	Renvoie un texte.
	"""
	type = quel_animal[randrange(len(quel_animal))]
	
	if type == "animal sauvage" :
		texte = "un "+animal_sauvage[randrange(len(animal_sauvage))]+" sauvage"
	
	elif type == "animal domestique" :
		texte = animal_domestique[randrange(len(animal_domestique))]+" appartenant à "
		texte += genere_affiche_perso_light()
	
	else :
		texte = "des "+animal_elevage[randrange(len(animal_elevage))]+"."

	return texte


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
	texte, cible = cible_infiltration()
	raison = raison_inf[randrange(len(raison_inf))]
	
	if raison == "voler" :
		texte += "\nIls pourront alors voler " + objet_pers[randrange(len(objet_pers))] + "."
	
	elif raison == "protéger" or raison == "libérer" or raison == "sauver" :
		texte += "\nIls pourront alors " + raison + " " + genere_affiche_perso_light()
	
	elif raison == "tuer" :
		metier = poste_dans(cible)
		texte += "\nIls pourront alors tuer " + gen_perso_def_metier(metier)
	
	else : #"détruire"
		texte += "\nIls pourront alors détruire cette organisation de l'intérieur."
	
	return texte


def cible_infiltration() :
	"""
	Quel réseau ou quelle organisation les héros doivent infiltrer.

	Renvoie deux textes.
	"""
	inf = infiltration[randrange(len(infiltration))]
	
	if inf == "un réseau" :
		cible = reseau[randrange(len(reseau))]
		texte = "un réseau " + cible + "."
	
	else : #"une organisation"
		cible = organisation[randrange(len(organisation))]
		texte = cible + "."
	
	return texte, cible


def mission_kidnaper() :
	"""
	Qui ou qu'est-ce que les héros doivent kidnaper.

	Renvoie un texte.
	"""
	cible = kid[randrange(len(kid))]
	
	if cible == "personne" :
		texte = genere_affiche_perso_light()  + "\nLa cible réside " + ou_en_ville()
	
	else : #"animal"
		cible = animal_domestique[randrange(len(animal_domestique))]
		texte = cible + " appartenant à "+genere_affiche_perso_light()
	
	return texte


def mission_detruire() :
	"""
	Ce que les héros doivent détruire et ou le trouver.

	Renvoie un texte.
	"""
	cible = destruction[randrange(len(destruction))]
	
	if cible == "un objet" :
		texte = objet_pers[randrange(len(objet_pers))] + " appartenant à "
		texte += genere_affiche_perso_light() + "\n\nCette personne vit " + ou_en_ville()

	elif cible == "une organisation" :
		texte = organisation[randrange(len(organisation))]+" " + ou_en_ville()
	
	elif cible == "un réseau" :
		texte = cible+" "+reseau[randrange(len(reseau))] + ".\nIls trouverons une de leurs câches "
		texte += lieu_discret[randrange(len(lieu_discret))] + " " + ou_en_ville()

	else :#"un bâtiment"
		texte = type_lieu_ville()
	
	return texte


def quel_monstre() :
	"""
	Génère un monstre (animal sacré ou créature) et l'endroit ou le trouver.

	Renvoie un texte.
	"""
	cible = monstre[randrange(len(monstre))]
	
	if cible == "animal sacré" :
		texte = animal_sacre()
		texte += " dans "+lieu_quete_ext()
	
	else : #"créature"
		texte = creature[randrange(len(creature))]
		texte += " dans "+lieu_quete()
	
	return texte


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
		texte = animal_domestique[randrange(len(animal_domestique))] + " appartenant à "
		texte += genere_affiche_perso_light() + "\nSa demeure se trouve " + ou_en_ville()

	elif cible ==  "une personne" :
		texte = genere_affiche_perso_light() + "\nSa demeure se trouve " + ou_en_ville()
	
	elif cible ==  "des caisses de nourriture" :
		texte = cible + ". Elles sont dans " + type_lieu_ville()
	
	else : #  "le puit d'un village"
		texte = "le puit " + ou_en_ville()
	
	return texte


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


