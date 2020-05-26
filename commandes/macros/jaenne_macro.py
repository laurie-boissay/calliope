"""
Les macros des personnages de Jaenne :  - Jaenne
                                        - Mérest
"""

from commandes.des import *
from commandes.caracteristiques import *

def macro_jaenne (macro_text) :
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
        return stat_w_of_d(qui, perso)

    elif len(macro_text) < 4:
        return perso + " saisit ses dés :" + short_w_of_d(macro_text)

    else:
        text = afficher_une_stat(qui, perso, macro_text)
        return text

def macro_merest (macro_text):
    perso = "Mérest"
    qui = carac_merest
    surprise = 5
    perception = 4
    odorat = 5
    survie = 4

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
        p2 = roll(1, 20, qui("dextérité") + qui("niveau"))
        return p1 + p2

    elif "!dmarbalète" in macro_text.lower():
        p1 = "Dégâts de l'arbalète légère de " + perso + " :\n"
        p2 = roll(2, 4, 2)
        return p1 + p2

    elif "!mlourde" in macro_text.lower():
        p1 = perso + " tire avec son arbalète lourde :\n"
        p2 = roll(1, 20, qui("dextérité") + qui("niveau") + 1)
        return p1 + p2

    elif "!dmlourde" in macro_text.lower():
        p1 = "Dégâts de l'arbalète lourde de " + perso + " :\n"
        p2 = roll(3, 4, 2)
        return p1 + p2

    elif "!mcouteau" in macro_text.lower():
        p1 = perso + " donne un coup de couteau :\n"
        p2 = roll(1, 20, qui("force") + qui("niveau"))
        return p1 + p2

    elif "!dmcouteau" in macro_text.lower():
        p1 = "Dégas du coup de couteau de " + perso + " :\n"
        p2 = roll(1, 4, 0)
        return p1 + p2

#______________Voies_____________________________________________

    elif "!msurprise" in macro_text.lower():
        p1 = perso + " est aux aguets (+ surprise + perception) :\n"
        p2 = roll(1, 20, qui("sagesse") +perception + surprise)
        return p1 + p2

    elif "!mperception" in macro_text.lower():
        p1 = perso + " fouille du regard (+perception) :\n"
        p2 = roll(1, 20, qui("sagesse") + perception)
        return p1 + p2

    elif "!mpistage" in macro_text.lower():
        p1 = perso + " cherche une piste (+ surprise + perception + odorat) :\n"
        p2 = roll(1, 20, qui("sagesse") + perception + odorat)
        return p1 + p2

    elif "!msurvie" in macro_text.lower():
        p1 = perso + " résiste aux éléments (+ survie) :\n"
        p2 = roll(1, 20, qui("constitution") + survie)
        return p1 + p2

#_____________Stats_______________________________________________

    elif "!mfor" in macro_text.lower():
        p1 = perso + " teste sa force :\n"
        p2 = roll(1, 20, qui("force"))
        return p1 + p2

    elif "!mdex" in macro_text.lower():
        p1 = perso + " teste sa dextérité :\n"
        p2 = roll(1, 20, qui("dextérité"))
        return p1 + p2

    elif "!mcon" in macro_text.lower():
        p1 = perso + " teste sa constitution :\n"
        p2 = roll(1, 20, qui("constitution"))
        return p1 + p2

    elif "!mint" in macro_text.lower():
        p1 = perso + " teste son intelligence :\n"
        p2 = roll(1, 20, qui("intelligence"))
        return p1 + p2

    elif "!msag" in macro_text.lower():
        p1 = perso + " teste sa sagesse :\n"
        p2 = roll(1, 20, qui("sagesse"))
        return p1 + p2

    elif "!mcha" in macro_text.lower():
        p1 = perso + " teste son charisme :\n"
        p2 = roll(1, 20, qui("charisme"))
        return p1 + p2

    elif "!mstat" in macro_text.lower():
        return stat_c_o(qui, perso)

    else:
        return "pas " + perso

def macro_jaenne_dm (macro_text) :
    if '!macro' in macro_text.lower():
        p1 = "\n\n```!jaenne```Affiche les macros pour Jaenne."
        p2 = "\n\n```!mérest```Affiche les macros pour Mérest Pala."
        return p1+p2

    elif '!jaenne' in macro_text.lower():
        text = ""
        macro_jaenne = [
        "\n\n```!i``` lance !2d6 + i"

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

        for ligne in range(len(macro_jaenne)):
            text += macro_jaenne[ligne]
        return text

    elif '!mérest' in macro_text.lower():
        text = ""
        macro_merest = [
        "\n\n```!carac```Affiche les macros concernant les caractéristiques de Mérest."
        "\n\n```!armes```Affiche les macros concernant les armes de Mérest."
        "\n\n```!voies```Affiche les macros concernant les voies de Mérest."
        "\n\n```!animaux```Affiche les macros concernant les animaux de Mérest."
        ]

        for ligne in range(len(macro_merest)):
            text += macro_merest[ligne]
        return text

    elif '!carac' in macro_text.lower():
        text = ""
        macro_merest = [
        "\n\n```!mstat```Affiche les caractéristiques de Mérest."
        "\n\n```!mfor```Mérest teste sa force."
        "\n\n```!mdex```Mérest teste sa dextérité."
        "\n\n```!mcon```Mérest teste sa constitution."
        "\n\n```!mint```Mérest teste son intelligence."
        "\n\n```!msag```Mérest teste sa sagesse."
        "\n\n```!mcha```Mérest teste son charisme."
        ]

        for ligne in range(len(macro_merest)):
            text += macro_merest[ligne]
        return text

    elif '!armes' in macro_text.lower():
        text = ""
        macro_merest = [
        "\n\n```!marbalète```Mérest tire avec son arbalète légère."
        "\n\n```!dmarbalète```Dégâts de l'arbalète légère de Mérest."
        "\n\n```!mlourde```Mérest tire avec son arbalète lourde."
        "\n\n```!dmlourde```Dégâts de l'arbalète lourde de Mérest."
        "\n\n```!mcouteau```Mérest donne un coup de couteau."
        "\n\n```!dmcouteau```Dégats du coup de couteau de Mérest.\n"
        ]

        for ligne in range(len(macro_merest)):
            text += macro_merest[ligne]
        return text

    elif '!voies' in macro_text.lower():
        text = ""
        macro_merest = [
        "\n\n```!mperception```Mérest fouille du regard (+ perception)."
        "\n\n```!msurprise```Mérest est aux aguets (+ surprise + perception)."
        "\n\n```!mpistage```Mérest cherche une piste (+ surprise + perception + odorat)."
        "\n\n```!msurvie```Mérest résiste aux éléments (+ survie).\n"
        ]

        for ligne in range(len(macro_merest)):
            text += macro_merest[ligne]
        return text

    elif '!animaux' in macro_text.lower():
        text = ""
        macro_merest = [
        "\n\n```!mdéfense```Pupuce donne un coup de défense."
        "\n\n```!dmdéfense```Dégâts du coup de défense."
        "\n\n```!mcharge```Pupuce charge."
        "\n\n```!dmcharge```Dégâts de la charge de Pupuce.\n"

        "\n\n```!mmorsure```Féroce mord."
        "\n\n```!dmmorsure```Dégâts de la morsure de Féroce.\n"
        ]

        for ligne in range(len(macro_merest)):
            text += macro_merest[ligne]
        return text

    else:
        return "pas perso"
