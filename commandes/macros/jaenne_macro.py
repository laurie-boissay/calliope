"""
Les macros des personnages de Jaenne :  - Jaenne
                                        - Mérest
"""

from commandes.des import *
from commandes.caracteristiques import *

def macro_personnages_jaenne(macro_text): 
    if (macro_text.startswith('!dm')) or (macro_text.startswith('!m')):
        text = macro_merest(macro_text)
       
    else:
        text = macro_jaenne(macro_text)

    return text

def macro_jaenne (macro_text):
    perso = "Jaenne"
    qui = carac_jaenne

    if "!darc" in macro_text.lower():
        p1 = "Dégâts du tir de " + perso + " :\n"
        p2 = roll(1, 6, 1)
        return p1 + p2

    elif "!dlance" in macro_text.lower():
        p1 = "Dégâts de l'attaque à la lance de " + perso + " :\n"
        p2 = roll(1, 6, 2)
        return p1 + p2

    if "!stat" in macro_text.lower():
        return toutes_stat(qui, perso)

    elif len(macro_text) < 4:
        return short_dice(macro_text, perso, 2, 6)


    elif len(macro_text) == 4:
        return afficher_une_stat(qui, perso, macro_text, 2, 6)

    else:
        return "not a macro"
    

def macro_merest (macro_text):
    perso = "Mérest"
    qui = carac_merest

#____________Pupuce_______________________________________________

    if "!mdéfense" in macro_text.lower():
        p1 = "Pupuce donne un coup de défense :\n"
        p2 = roll(1, 20, 4)
        return p1 + p2

    elif "!dmdéfense" in macro_text.lower():
        p1 = "Dégâts du coup de défense :\n"
        p2 = roll(1, 6, 3)
        return p1 + p2

    elif "!mcharge" in macro_text.lower():
        text = "Pupuce charge (choisir le meilleur résultat) :\n"
        for loop in range (2):
            text += roll(1, 20, 4)
        return text

    elif "!dmcharge" in macro_text.lower():
        p1 = "Dégâts de la charge de Pupuce (résultat x 2) :\n"
        p2 = roll(1, 6, 3)
        return p1 + p2

#____________Féroce_______________________________________________

    elif "!mmorsure" in macro_text.lower():
        p1 = "Féroce mord :\n"
        p2 = roll(1, 20, 1)
        return p1 + p2

    elif "!dmmorsure" in macro_text.lower():
        p1 = "Dégâts de la morsure de Féroce :\n"
        p2 = roll(1, 6, 1)
        return p1 + p2

#______________Armes_____________________________________________

    elif "!marbalète" in macro_text.lower():
        p1 = "Mérest tire avec son arbalète légère :\n"
        p2 = roll(1, 20, qui["dextérité"] + qui["niveau"])
        return p1 + p2

    elif "!dmarbalète" in macro_text.lower():
        p1 = "Dégâts de l'arbalète légère de " + perso + " :\n"
        p2 = roll(2, 4, 2)
        return p1 + p2

    elif "!mlourde" in macro_text.lower():
        p1 = perso + " tire avec son arbalète lourde :\n"
        p2 = roll(1, 20, qui["dextérité"] + qui["niveau"] + 1)
        return p1 + p2

    elif "!dmlourde" in macro_text.lower():
        p1 = "Dégâts de l'arbalète lourde de " + perso + " :\n"
        p2 = roll(3, 4, 2)
        return p1 + p2

    elif "!mcouteau" in macro_text.lower():
        p1 = perso + " donne un coup de couteau :\n"
        p2 = roll(1, 20, qui("force") + qui["niveau"])
        return p1 + p2

    elif "!dmcouteau" in macro_text.lower():
        p1 = "Dégas du coup de couteau de " + perso + " :\n"
        p2 = roll(1, 4, 0)
        return p1 + p2

#______________Voies_____________________________________________

    elif "!msurprise" in macro_text.lower():
        p1 = perso + " est aux aguets (+ surprise + perception) :\n"
        p2 = roll(1, 20, qui["sagesse"] + qui["perception"] + qui["surprise"])
        return p1 + p2

    elif "!mperception" in macro_text.lower():
        p1 = perso + " fouille du regard (+perception) :\n"
        p2 = roll(1, 20, qui["sagesse"] + qui["perception"])
        return p1 + p2

    elif "!mpistage" in macro_text.lower():
        p1 = perso + " cherche une piste (+ perception + odorat) :\n"
        p2 = roll(1, 20, qui["sagesse"] + qui["perception"] + qui["odorat"])
        return p1 + p2

    elif "!msurvie" in macro_text.lower():
        p1 = perso + " résiste aux éléments (+ survie) :\n"
        p2 = roll(1, 20, qui["constitution"] + qui["survie"])
        return p1 + p2

#_____________Stats_______________________________________________

    elif len(macro_text) == 5:
        return afficher_une_stat(qui, perso, macro_text, 1, 20)

    else:
        return "not a macro"

def macro_jaenne_dm (macro_text) :
    if '!macro' in macro_text.lower():
        text =[
        "\n\n```!jaenne```Affiche les macros pour Jaenne."
        "\n\n```!mérest```Affiche les macros pour Mérest Pala."
        ]
        return text[0]

    elif '!jaenne' in macro_text.lower():
        text = [
        "\n\n```!i``` lance !2d6 + i pour i valant de -9 à 99 sans signe + devant i."

        "\n\n```!darc```Dégâts du tir de Jaenne."
        "\n\n```!dlance```Dégâts de l'attaque à la lance de Jaenne.\n"

        "\n\n```!stat```Affiche les caractéristiques de Jaenne.\n"

        "\n\n```!for```Jaenne teste sa force."
        "\n\n```!dex```Jaenne teste sa dextérité."
        "\n\n```!con```Jaenne teste sa constitution."
        "\n\n```!int```Jaenne teste son intelligence."
        "\n\n```!sag```Jaenne teste sa sagesse."
        "\n\n```!cha```Jaenne teste son charisme."
        ]
        return text[0]

    elif '!mérest' in macro_text.lower():
        text = [
        "\n\n```!carac```Affiche les macros concernant les caractéristiques de Mérest."
        "\n\n```!armes```Affiche les macros concernant les armes de Mérest."
        "\n\n```!voies```Affiche les macros concernant les voies de Mérest."
        "\n\n```!animaux```Affiche les macros concernant les animaux de Mérest."
        ]
        return text[0]

    elif '!carac' in macro_text.lower():
        text = [
        "\n\n```!mstat```Affiche les caractéristiques de Mérest."
        "\n\n```!mfor```Mérest teste sa force."
        "\n\n```!mdex```Mérest teste sa dextérité."
        "\n\n```!mcon```Mérest teste sa constitution."
        "\n\n```!mint```Mérest teste son intelligence."
        "\n\n```!msag```Mérest teste sa sagesse."
        "\n\n```!mcha```Mérest teste son charisme."
        ]
        return text[0]

    elif '!armes' in macro_text.lower():
        text = [
        "\n\n```!marbalète```Mérest tire avec son arbalète légère."
        "\n\n```!dmarbalète```Dégâts de l'arbalète légère de Mérest."
        "\n\n```!mlourde```Mérest tire avec son arbalète lourde."
        "\n\n```!dmlourde```Dégâts de l'arbalète lourde de Mérest."
        "\n\n```!mcouteau```Mérest donne un coup de couteau."
        "\n\n```!dmcouteau```Dégats du coup de couteau de Mérest.\n"
        ]
        return text[0]

    elif '!voies' in macro_text.lower():
        text = [
        "\n\n```!mperception```Mérest fouille du regard (+ perception)."
        "\n\n```!msurprise```Mérest est aux aguets (+ surprise + perception)."
        "\n\n```!mpistage```Mérest cherche une piste (+ surprise + perception + odorat)."
        "\n\n```!msurvie```Mérest résiste aux éléments (+ survie).\n"
        ]
        return text[0]

    elif '!animaux' in macro_text.lower():
        text = [
        "\n\n```!mdéfense```Pupuce donne un coup de défense."
        "\n\n```!dmdéfense```Dégâts du coup de défense."
        "\n\n```!mcharge```Pupuce charge."
        "\n\n```!dmcharge```Dégâts de la charge de Pupuce.\n"

        "\n\n```!mmorsure```Féroce mord."
        "\n\n```!dmmorsure```Dégâts de la morsure de Féroce.\n"
        ]
        return text[0]

    else:
        return "pas perso"
