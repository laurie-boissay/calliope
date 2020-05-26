"""
Les macro du personnage de Mel : Willow.
"""

from commandes.des import *
from commandes.caracteristiques import *

def macro_willow (macro_text) :
    perso = "Willow"
    qui = carac_willow

    if "!stat" in macro_text.lower():
        return stat_w_of_d(qui, perso)

    elif len(macro_text) < 4:
        return perso + " saisit ses dés :" + short_w_of_d(macro_text)

    else:
        text = afficher_une_stat(qui, perso, macro_text)
        return text  

def macro_mel_dm (macro_text) :
    if '!macro' in macro_text.lower():
        p1 = "\n\n```!willow```Affiche les macros pour Willow."
        return p1

    elif '!willow' in macro_text.lower():
        text = ""
        macro_willow = [
        "\n\n```!'i'``` Effectue !2d6 + 'i'"
        "\n\n```!stat```Affiche les caractéristiques de Willow."
        "\n\n```!for```Willow teste sa force."
        "\n\n```!dex```Willow teste sa dextérité."
        "\n\n```!con```Willow teste sa constitution."
        "\n\n```!int```Willow teste son intelligence."
        "\n\n```!sag```Willow teste sa sagesse."
        "\n\n```!cha```Willow teste son charisme."
        ]

        for ligne in range(len(macro_willow)):
            text += macro_willow[ligne]
        return text

    else:
        return "pas perso"
