"""
Les caractéristiques des joueurs de mon serveur ;
Les fonctions qui font appel à ses caractéristiques.
"""

from commandes.des import *


#______World_of_dungeons______________________________________

def carac_darius(carac) :

    caracteristiques = {
    "force" : 0,
    "dextérité" : 0,
    "constitution" : 0,
    "intelligence" : 0,
    "sagesse" : 0,
    "charisme" : 0
    }

    for caracteristique, valeur in caracteristiques.items():
        if caracteristique == carac:
            return valeur

def carac_duncan(carac) :

    caracteristiques = {
    "force" : 0,
    "dextérité" : -1,
    "constitution" : 2,
    "intelligence" : 2,
    "sagesse" : 1,
    "charisme" : 1
    }

    for caracteristique, valeur in caracteristiques.items():
        if caracteristique == carac:
            return valeur

def carac_filtch(carac) :

    caracteristiques = {
    "force" : -1,
    "dextérité" : 2,
    "constitution" : 0,
    "intelligence" : 2,
    "sagesse" : 0,
    "charisme" : 1
    }

    for caracteristique, valeur in caracteristiques.items():
        if caracteristique == carac:
            return valeur

def carac_jaenne(carac) :

    caracteristiques = {
    "force" : -1,
    "dextérité" : 0,
    "constitution" : 0,
    "intelligence" : 1,
    "sagesse" : 1,
    "charisme" : 2
    }

    for caracteristique, valeur in caracteristiques.items():
        if caracteristique == carac:
            return valeur

def carac_willow(carac) :

    caracteristiques = {
    "force" : 1,
    "dextérité" : 2,
    "constitution" : 0,
    "intelligence" : 1,
    "sagesse" : 0,
    "charisme" : -1
    }

    for caracteristique, valeur in caracteristiques.items():
        if caracteristique == carac:
            return valeur

def stat_w_of_d(qui, perso):
    text = "Caractéristiques de " + perso + " : \n"
    liste_carac = [
    "force", "dextérité", "constitution", 
    "intelligence", "sagesse", "charisme"
    ]
    for caracteristiques in range(len(liste_carac)):
        text += liste_carac[caracteristiques].capitalize() + " : " + str(qui(liste_carac[caracteristiques])) + "\n"
    return text

def afficher_une_stat(qui, perso, macro_text):

    if "!for" in macro_text.lower():
        carac = "force"
        text = perso + " teste sa " + carac + " : " + roll(2, 6, qui(carac))

    elif "!dex" in macro_text.lower():
        carac = "dextérité"
        text = perso + " teste sa " + carac + " : " + roll(2, 6, qui(carac))

    elif "!con" in macro_text.lower():
        carac = "constitution"
        text = perso + " teste sa " + carac + " : " + roll(2, 6, qui(carac))

    elif "!int" in macro_text.lower():
        carac = "intelligence"
        text = perso + " teste son " + carac + " : " + roll(2, 6, qui(carac))

    elif "!sag" in macro_text.lower():
        carac = "sagesse"
        text = perso + " teste sa " + carac + " : " + roll(2, 6, qui(carac))

    elif "!cha" in macro_text.lower():
        carac = "charisme"
        text = perso + " teste son " + carac + " : " + roll(2, 6, qui(carac))

    else:
        text = "pas " + perso
    
    return text

#______Chroniques_oubliées______________________________________

def carac_eustache(carac) :
    caracteristiques = {
    "force" : 0,
    "dextérité" : 1,
    "constitution" : 0,
    "intelligence" : 3,
    "sagesse" : 0,
    "charisme" : 0,
    "initiative" : 0,
    "défense" : 0,
    "niveau" : 2
    }

    for caracteristique, valeur in caracteristiques.items():
        if caracteristique == carac:
            return valeur

def carac_gargrim(carac) :
    caracteristiques = {
    "force" : 3,
    "dextérité" : 1,
    "constitution" : 3,
    "intelligence" : 0,
    "sagesse" : 0,
    "charisme" : 1,
    "initiative" : 4,
    "défense" : 19,
    "niveau" : 3
    }

    for caracteristique, valeur in caracteristiques.items():
        if caracteristique == carac:
            return valeur


def carac_merest(carac) :
    caracteristiques = {
    "force" : 0,
    "dextérité" : 4,
    "constitution" : 2,
    "intelligence" : 0,
    "sagesse" : 2,
    "charisme" : 0,
    "initiative" : 9,
    "défense" : 16,
    "niveau" : 3
    }

    for caracteristique, valeur in caracteristiques.items():
        if caracteristique == carac:
            return valeur

def stat_c_o(qui, perso):
    text = "Caractéristiques de " + perso + " : \n"
    liste_carac = [
    "force", "dextérité", "constitution", 
    "intelligence", "sagesse", "charisme",
    "initiative", "défense", "niveau" 
    ]
    for caracteristiques in range(len(liste_carac)):
        text += liste_carac[caracteristiques].capitalize() + " : " + str(qui(liste_carac[caracteristiques])) + "\n"
    return text

def afficher_1_stat(qui, perso, macro_text):

    if "!for" in macro_text.lower():
        carac = "force"
        text = perso + " teste sa " + carac + roll(2, 6, qui(carac))

    elif "!dex" in macro_text.lower():
        carac = "dextérité"
        text = perso + " teste sa " + carac + roll(2, 6, qui(carac))

    elif "!con" in macro_text.lower():
        carac = "constitution"
        text = perso + " teste sa " + carac + roll(2, 6, qui(carac))

    elif "!int" in macro_text.lower():
        carac = "intelligence"
        text = perso + " teste son " + carac + roll(2, 6, qui(carac))

    elif "!sag" in macro_text.lower():
        carac = "sagesse"
        text = perso + " teste sa " + carac + roll(2, 6, qui(carac))

    elif "!cha" in macro_text.lower():
        carac = "charisme"
        text = perso + " teste son " + carac + roll(2, 6, qui(carac))

    else:
        text = "pas " + perso
    
    return text
