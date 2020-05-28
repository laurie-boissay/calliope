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
        return afficher_une_stat(qui, perso, macro_text)

def macro_stevendeo_dm (macro_text) :
    if '!macro' in macro_text.lower():
        return "\n\n```!duncan```Affiche les macros pour Duncan."

    elif '!duncan' in macro_text.lower():
        text = [
        "\n\n```!'i'```lance !2d6 + i pour i valant de -9 à 99 sans signe + devant i."
        "\n\n```!stat```Affiche les caractéristiques de Duncan."
        "\n\n```!for```Duncan teste sa force."
        "\n\n```!dex```Duncan teste sa dextérité."
        "\n\n```!con```Duncan teste sa constitution."
        "\n\n```!int```Duncan teste son intelligence."
        "\n\n```!sag```Duncan teste sa sagesse."
        "\n\n```!cha```Duncan teste son charisme."
        ]
        return text[0]

    else:
        return "pas perso"
