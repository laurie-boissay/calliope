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

def texte_de_quete(message):
	quete = Quete()

	quete.set_mission_commanditaire(message)
	quete.combler_les_manques()

	text = quete.assembler_texte_de_quete()

	return text