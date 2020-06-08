#!/usr/bin/python3.8
#coding:u8

from random import randrange

from collection_de_mots.quetes import *
from collection_de_mots.zone import *
from collection_de_mots.personnes import *
from collection_de_mots.activites import *
from collection_de_mots.trucs import *

from generer.perso import *
from generer.classe_quete import Quete
from generer.classe_zone import Zone


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
