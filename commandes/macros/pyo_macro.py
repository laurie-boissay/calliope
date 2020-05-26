"""
Les macro du personnage de PYo : Eustache.
"""

from commandes.des import *
from commandes.caracteristiques import *

def macro_eustache (macro_text) :
    perso = "Eustache"
    qui = carac_eustache

    if "!arbalète" in macro_text.lower():
        p1 = "Eustache tire à l'arbalète :\n" 
        p2 = roll(1, 20, qui("dextérité") + qui("niveau")) 
        return p1 + p2

#______Dégâts____________________________________________________________________

    elif "!darbalète" in macro_text.lower():
        p1 = "Dégâts de l'arbalète de Eustache :\n" 
        p2 = roll(2, 4, 0) 
        return p1 + p2

#________voies_______________________________________________________________________

    elif "!sort" in macro_text.lower():
        p1 = "Eustache lance un sort :\n" 
        p2 = roll(1, 20, qui("intelligence") + qui("niveau"))
        return p1 + p2


#______Tests stats____________________________________________________________________
    
    elif "!stat" in macro_text.lower():
        return stat_c_o(qui, perso)

    elif len(macro_text) < 4:
        return perso + " saisit ses dés :" + short_c_o(macro_text)
    
    else:
        text = afficher_1_stat(qui, perso, macro_text)
        return text

#_____________________________________________________________________________________


def macro_pyo_dm (macro_text) :
    if '!macro' in macro_text.lower():
        p1 = "\n\n```!eustache```Affiche les macros pour Eustache."
        return p1

    elif '!eustache' in macro_text.lower():
        text = ""
        macro_eustache = [
        "\n\n```!i```Lance !1d20 + i"
        "\n\n```!carac```Affiche les macros concernant les caractéristiques de Eustache."
        "\n\n```!armes```Affiche les macros concernant les armes de Eustache."
        "\n\n```!voies```Affiche les macros concernant les voies de Eustache."
        ]

        for ligne in range(len(macro_eustache)):
            text += macro_eustache[ligne]
        return text

    elif '!carac' in macro_text.lower():
        text = ""
        macro_eustache = [
        "\n\n```!stat```Affiche les caractéristiques de Eustache."
        "\n\n```!ini```Affiche l'initiative de Eustache."
        "\n\n```!déf```Affiche la défense de Eustache."
        "\n\n```!for```Eustache teste sa force."
        "\n\n```!dex```Eustache teste sa dextérité."
        "\n\n```!con```Eustache teste sa constitution."
        "\n\n```!int```Eustache teste son intelligence."
        "\n\n```!sag```Eustache teste sa sagesse."
        "\n\n```!cha```Eustache teste son charisme."
        ]

        for ligne in range(len(macro_eustache)):
            text += macro_eustache[ligne]
        return text

    elif '!armes' in macro_text.lower():
        text = ""
        macro_eustache = [
        "\n\n```!arbalète```Eustache tire à l'arbalète."
        "\n\n```!darbalète```Dégâts de l'arbalète de Eustache."
        ]

        for ligne in range(len(macro_eustache)):
            text += macro_eustache[ligne]
        return text

    elif '!voies' in macro_text.lower():
        text = ""
        macro_eustache = [
        "\n\n```!sort```Eustache lance un sort."
        ]

        for ligne in range(len(macro_eustache)):
            text += macro_eustache[ligne]
        return text

    else:
        return "pas perso"