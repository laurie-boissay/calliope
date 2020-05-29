#!/usr/bin/python3.8
#coding:u8


"""
Les caractéristiques des joueurs de mon serveur ;
Les fonctions qui font appel à ces caractéristiques.
"""

from commandes.des import *

carac_darius = {
    "force" : 0,
    "dextérité" : 0,
    "constitution" : 0,
    "intelligence" : 0,
    "sagesse" : 0,
    "charisme" : 0
    }

carac_duncan = {
    "force" : 0,
    "dextérité" : -1,
    "constitution" : 2,
    "intelligence" : 2,
    "sagesse" : 1,
    "charisme" : 1
    }

carac_eustache = {
    "force" : 0,
    "dextérité" : 1,
    "constitution" : 0,
    "intelligence" : 3,
    "sagesse" : 1,
    "charisme" : 3,
    "initiative" : 3,
    "défense" : 14,
    "niveau" : 2,
    "arme de maître" : 1,
    "surprise" : 4,
    }

carac_filtch = {
    "force" : -1,
    "dextérité" : 2,
    "constitution" : 0,
    "intelligence" : 2,
    "sagesse" : 0,
    "charisme" : 1
    }

carac_gargrim = {
    "force" : 3,
    "dextérité" : 1,
    "constitution" : 3,
    "intelligence" : 0,
    "sagesse" : 0,
    "charisme" : 1,
    "initiative" : 4,
    "défense" : 19,
    "niveau" : 3,
    "gantelets" : 2,
    "maitre_arme" : 1,
    }

carac_jaenne = {
    "force" : -1,
    "dextérité" : 0,
    "constitution" : 0,
    "intelligence" : 1,
    "sagesse" : 1,
    "charisme" : 2,
    "armure" : 1,
    }

carac_merest = {
    "force" : 0,
    "dextérité" : 4,
    "constitution" : 2,
    "intelligence" : 0,
    "sagesse" : 2,
    "charisme" : 0,
    "initiative" : 9,
    "défense" : 16,
    "niveau" : 3,
    "surprise" : 5,
    "odorat" : 5,
    "survie" : 4,
    "perception" : 4
    }

carac_willow = {
    "force" : 1,
    "dextérité" : 2,
    "constitution" : 0,
    "intelligence" : 1,
    "sagesse" : 0,
    "charisme" : -1,
    "bonus de dégâts arc" : 2,
    }

def toutes_stat(qui, perso):
    text = "Caractéristiques de " + perso + " : \n"
    for k, v in qui.items():
        text += k.capitalize() + " : " + str(v) + "\n"
    return text

def afficher_une_stat(qui, perso, macro_text, nb_des, valeur_des):
    commandes_stat = {
    "for" : "force",
    "dex" : "dextérité",
    "con" : "constitution",
    "int" : "intelligence",
    "sag" : "sagesse",
    "cha" : "charisme" 
    }

    for k, v in commandes_stat.items():
        if k.strip("!") in macro_text.lower():        
            return perso + " teste une caractéristique : " + v + " :\n" + roll(nb_des, valeur_des, qui[v])
    return "not a macro"


#cd /home/jaenne/Python/calliope/commandes
# ./caracteristiques_modif.py