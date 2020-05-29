"""
Les macro du personnage de Mel : Willow.
"""

from commandes.des import *
from commandes.caracteristiques import *

def macro_willow (macro_text) :
    perso = "Willow"
    qui = carac_willow

    if "!stat" in macro_text.lower():
        return toutes_stat(qui, perso)

    if "!darc" in macro_text.lower():
        p1 = "Dégâts du tir de " + perso + " + (bonus de dégâts arc) :\n"
        p2 = roll(1, 6, 1 + qui["bonus de dégâts arc"])
        return p1 + p2

    elif len(macro_text) < 4:
        return short_dice(macro_text, perso, 2, 6)

    elif len(macro_text) == 4:
        return afficher_une_stat(qui, perso, macro_text, 2, 6)

    else:
        return "not a macro"

def macro_mel_dm (macro_text) :
    if '!macro' in macro_text.lower():
        return "\n\n```!willow```Affiche les macros pour Willow."

    elif '!willow' in macro_text.lower():
        text = [
        "\n\n```!'i'```lance !2d6 + i pour i valant de -9 à 99 sans signe + devant i."
        "\n\n```!stat```Affiche les caractéristiques de Willow."
        "\n\n```!for```Willow teste sa force."
        "\n\n```!dex```Willow teste sa dextérité."
        "\n\n```!con```Willow teste sa constitution."
        "\n\n```!int```Willow teste son intelligence."
        "\n\n```!sag```Willow teste sa sagesse."
        "\n\n```!cha```Willow teste son charisme."
        "\n\n```!darc```Dégats de l'arc de Willow avec bonus + 2."
        ]
        return text[0]

    else:
        return "pas perso"
