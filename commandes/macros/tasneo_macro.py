"""
Les macro du personnage de tasneo : Darius.
"""

from commandes.des import *
from commandes.caracteristiques import *

def macro_darius (macro_text) :
    perso = "Darius"
    qui = carac_darius

    if "!stat" in macro_text.lower():
        return toutes_stat(qui, perso)

    elif len(macro_text) < 4:
        return perso + " saisit ses dés :" + short_w_of_d(macro_text)

    else:
        text = afficher_une_stat(qui, perso, macro_text)
        return text

def macro_tasneo_dm (macro_text) :
    if '!macro' in macro_text.lower():
        p1 = "\n\n```!darius```Affiche les macros pour darius."
        return p1

    elif '!darius' in macro_text.lower():
        text = ""
        macro_darius = [
        "\n\n```!i```Lance !2d6 + i"
        "\n\n```!stat```Affiche les caractéristiques de Darius."
        "\n\n```!for```Darius teste sa force."
        "\n\n```!dex```Darius teste sa dextérité."
        "\n\n```!con```Darius teste sa constitution."
        "\n\n```!int```Darius teste son intelligence."
        "\n\n```!sag```Darius teste sa sagesse."
        "\n\n```!cha```Darius teste son charisme."
        ]

        for ligne in range(len(macro_darius)):
            text += macro_darius[ligne]
        return text

    else:
        return "pas perso"
