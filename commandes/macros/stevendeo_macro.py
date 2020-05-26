"""
Les macro du personnage de Stevendeo : Duncan.
"""

from commandes.des import *
from commandes.caracteristiques import *

def macro_duncan (macro_text) :
    perso = "Duncan"
    qui = carac_duncan
    
    if "!stat" in macro_text.lower():
        return toutes_stat(qui, perso)

    elif len(macro_text) < 4:
        return perso + " saisit ses dés :" + short_w_of_d(macro_text)

    else:
        text = afficher_une_stat(qui, perso, macro_text)
        return text

def macro_stevendeo_dm (macro_text) :
    if '!macro' in macro_text.lower():
        p1 = "\n\n```!duncan```Affiche les macros pour Duncan."
        return p1

    elif '!duncan' in macro_text.lower():
        text = ""
        macro_duncan = [
        "\n\n```!'i'``` Effectue !2d6 + 'i'"
        "\n\n```!stat```Affiche les caractéristiques de Duncan."
        "\n\n```!for```Duncan teste sa force."
        "\n\n```!dex```Duncan teste sa dextérité."
        "\n\n```!con```Duncan teste sa constitution."
        "\n\n```!int```Duncan teste son intelligence."
        "\n\n```!sag```Duncan teste sa sagesse."
        "\n\n```!cha```Duncan teste son charisme."
        ]

        for ligne in range(len(macro_duncan)):
            text += macro_duncan[ligne]
        return text

    else:
        return "pas perso"
