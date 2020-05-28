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
        return afficher_une_stat(qui, perso, macro_text)

def macro_tasneo_dm (macro_text) :
    if '!macro' in macro_text.lower():
        return "\n\n```!darius```Affiche les macros pour darius."

    elif '!darius' in macro_text.lower():
        text = [
        "\n\n```!i```lance !2d6 + i pour i valant de -9 à 99 sans signe + devant i."
        "\n\n```!stat```Affiche les caractéristiques de Darius."
        "\n\n```!for```Darius teste sa force."
        "\n\n```!dex```Darius teste sa dextérité."
        "\n\n```!con```Darius teste sa constitution."
        "\n\n```!int```Darius teste son intelligence."
        "\n\n```!sag```Darius teste sa sagesse."
        "\n\n```!cha```Darius teste son charisme."
        ]
        return text[0]

    else:
        return "pas perso"
