"""
Les macros du personnage de Jaenne : Mérest
"""

from commandes.des import *
from commandes.caracteristiques import *


def macro_merest (macro_text):
    perso = "Mérest"
    qui = carac_merest

#____________Pupuce_______________________________________________

    if "!défense" in macro_text.lower():
        p1 = "Pupuce donne un coup de défense :\n"
        p2 = roll(1, 20, 4)
        return p1 + p2

    elif "!ddéfense" in macro_text.lower():
        p1 = "Dégâts du coup de défense :\n"
        p2 = roll(1, 6, 3)
        return p1 + p2

    elif "!charge" in macro_text.lower():
        text = "Pupuce charge (choisir le meilleur résultat) :\n"
        for loop in range (2):
            text += roll(1, 20, 4)
        return text

    elif "!dcharge" in macro_text.lower():
        p1 = "Dégâts de la charge de Pupuce (résultat x 2) :\n"
        p2 = roll(1, 6, 3)
        return p1 + p2

#____________Féroce_______________________________________________

    elif "!morsure" in macro_text.lower():
        p1 = "Féroce mord :\n"
        p2 = roll(1, 20, 1)
        return p1 + p2

    elif "!dmorsure" in macro_text.lower():
        p1 = "Dégâts de la morsure de Féroce :\n"
        p2 = roll(1, 6, 1)
        return p1 + p2

#______________Armes_____________________________________________

    elif "!arbalète" in macro_text.lower():
        p1 = "Mérest tire avec son arbalète légère :\n"
        p2 = roll(1, 20, qui["dextérité"] + qui["niveau"])
        return p1 + p2

    elif "!darbalète" in macro_text.lower():
        p1 = "Dégâts de l'arbalète légère de " + perso + " :\n"
        p2 = roll(2, 4, 2)
        return p1 + p2

    elif "!lourde" in macro_text.lower():
        p1 = perso + " tire avec son arbalète lourde :\n"
        p2 = roll(1, 20, qui["dextérité"] + qui["niveau"] + 1)
        return p1 + p2

    elif "!dlourde" in macro_text.lower():
        p1 = "Dégâts de l'arbalète lourde de " + perso + " :\n"
        p2 = roll(3, 4, 2)
        return p1 + p2

    elif "!couteau" in macro_text.lower():
        p1 = perso + " donne un coup de couteau :\n"
        p2 = roll(1, 20, qui("force") + qui["niveau"])
        return p1 + p2

    elif "!dcouteau" in macro_text.lower():
        p1 = "Dégâts du coup de couteau de " + perso + " :\n"
        p2 = roll(1, 4, 0)
        return p1 + p2

#______________Voies_____________________________________________

    elif "!surprise" in macro_text.lower():
        p1 = perso + " est aux aguets (+ surprise + perception) :\n"
        p2 = roll(1, 20, qui["sagesse"] + qui["perception"] + qui["surprise"])
        return p1 + p2

    elif "!perception" in macro_text.lower():
        p1 = perso + " fouille du regard (+perception) :\n"
        p2 = roll(1, 20, qui["sagesse"] + qui["perception"])
        return p1 + p2

    elif "!pistage" in macro_text.lower():
        p1 = perso + " cherche une piste (+ perception + odorat) :\n"
        p2 = roll(1, 20, qui["sagesse"] + qui["perception"] + qui["odorat"])
        return p1 + p2

    elif "!survie" in macro_text.lower():
        p1 = perso + " résiste aux éléments (+ survie) :\n"
        p2 = roll(1, 20, qui["constitution"] + qui["survie"])
        return p1 + p2


#__________!i___________________________________________________________________________
    elif len(macro_text) < 4:
        return short_dice(macro_text, perso, 1, 20)


#_____________Stats_______________________________________________
    elif "!stat" in macro_text.lower():
        return toutes_stat(qui, perso)
    
    elif len(macro_text) == 4:
        return afficher_une_stat(qui, perso, macro_text, 1, 20)
    else:
        return "not a macro"


def macro_jaenne_dm (macro_text) :
    if '!macro' in macro_text.lower():
        text =[
        "\n\n```!mérest```Affiche les macros pour Mérest Pala."
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
        "\n\n```!stat```Affiche les caractéristiques de Mérest."
        "\n\n```!for```Mérest teste sa force."
        "\n\n```!dex```Mérest teste sa dextérité."
        "\n\n```!con```Mérest teste sa constitution."
        "\n\n```!int```Mérest teste son intelligence."
        "\n\n```!sag```Mérest teste sa sagesse."
        "\n\n```!cha```Mérest teste son charisme."
        ]
        return text[0]

    elif '!armes' in macro_text.lower():
        text = [
        "\n\n```!arbalète```Mérest tire avec son arbalète légère."
        "\n\n```!darbalète```Dégâts de l'arbalète légère de Mérest."
        "\n\n```!lourde```Mérest tire avec son arbalète lourde."
        "\n\n```!dlourde```Dégâts de l'arbalète lourde de Mérest."
        "\n\n```!couteau```Mérest donne un coup de couteau."
        "\n\n```!dcouteau```Dégats du coup de couteau de Mérest.\n"
        ]
        return text[0]

    elif '!voies' in macro_text.lower():
        text = [
        "\n\n```!perception```Mérest fouille du regard (+ perception)."
        "\n\n```!surprise```Mérest est aux aguets (+ surprise + perception)."
        "\n\n```!pistage```Mérest cherche une piste (+ surprise + perception + odorat)."
        "\n\n```!survie```Mérest résiste aux éléments (+ survie).\n"
        ]
        return text[0]

    elif '!animaux' in macro_text.lower():
        text = [
        "\n\n```!défense```Pupuce donne un coup de défense."
        "\n\n```!ddéfense```Dégâts du coup de défense."
        "\n\n```!charge```Pupuce charge."
        "\n\n```!dcharge```Dégâts de la charge de Pupuce.\n"
        "\n\n```!morsure```Féroce mord."
        "\n\n```!dmorsure```Dégâts de la morsure de Féroce.\n"
        ]
        return text[0]

    else:
        return "pas perso"
