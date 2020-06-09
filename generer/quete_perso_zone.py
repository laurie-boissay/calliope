#!/usr/bin/python3.8
#coding:u8

from random import randrange

from collection_de_mots.quetes import *
from collection_de_mots.zone import *
from collection_de_mots.personnes import *
from collection_de_mots.activites import *
from collection_de_mots.trucs import *

from generer.classe_quete import Quete
from generer.classe_zone import Zone
from generer.classe_personnage import Personnage


def texte_de_quete(message):
	"""
	Permet de lancer la génération d'une quête.
	Renvoie un texte.
	"""
	quete = Quete()

	quete.set_mission_commanditaire(message)
	quete.combler_les_manques()

	return quete.assembler_texte_de_quete()


def texte_description_zone(message):
	"""
	Permet de lancer la génération d'une zone.
	Renvoie un texte.
	"""
	zone = Zone()	

	zone.contraintes(message)
	zone.set_zone()

	return zone.get_zone_nom() + " :\n\n" + zone.set_description()


def texte_description_perso(message):
	"""
	Prend une commande utilisateur en argument.

	Appelle la classe Personnage.

	Appelle certaines fonction de la classe Personnage
	afin de générer un personage généré semi-aléatoirement 
	correspondant aux souhaits de l'utilisateur.

	Renvoie un texte décrivant le personnage.
	
	"""
	text = [""]
	perso = Personnage()

	perso.set_cmd_text(message)
	perso.set_type_de_personnage()
	
	text[0], cmd = perso.set_total_points_et_valeur_max()
	if not cmd :
		return text[0]
	
	perso.set_param_identite()
	perso.set_param_proscrits()
	perso.set_particularites()
	perso.bonus_de_metier()

	return perso.afficher_personnage()
