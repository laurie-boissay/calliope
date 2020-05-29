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
        p2 = roll(1, 20, qui["dextérité"] + qui["niveau"]) 
        return p1 + p2

    elif "!dague" in macro_text.lower():
        p1 = "Eustache donne un coup de dague :\n" 
        p2 = roll(1, 20, qui("force") + qui["niveau"]) 
        return p1 + p2

    elif "!lpierres" in macro_text.lower():
        p1 = "Eustache tire au lance-pierres :\n" 
        p2 = roll(1, 20, qui["dextérité"] + qui["niveau"]) 
        return p1 + p2

    elif "!rapière" in macro_text.lower():
        p1 = "Eustache donne un coup de rapière :\n" 
        p2 = roll(1, 20, qui["dextérité"] + qui["niveau"] + qui["arme de maître"]) 
        return p1 + p2

#______Dégâts____________________________________________________________________

    elif "!darbalète" in macro_text.lower():
        p1 = "Dégâts de l'arbalète d'Eustache :\n" 
        p2 = roll(1, 6, 0) 
        return p1 + p2

    elif "!ddague" in macro_text.lower():
        p1 = "Dégâts de la dague d'Eustache :\n" 
        p2 = roll(1, 4, 0) 
        return p1 + p2

    elif "!dlpierres" in macro_text.lower():
        p1 = "Dégâts du lance-pierres d'Eustache :\n" 
        p2 = roll(1, 4, 0) 
        return p1 + p2

    elif "!drapière" in macro_text.lower():
        p1 = "Dégâts de la rapière d'Eustache :\n" 
        p2 = roll(1, 6, 0) 
        return p1 + p2

#________voies_______________________________________________________________________

    elif "!sort" in macro_text.lower():
        p1 = "Eustache lance un sort :\n" 
        p2 = roll(1, 20, qui["intelligence"] + qui["niveau"])
        return p1 + p2

    elif "!surprise" in macro_text.lower():
        p1 = "Eustache est aux aguets :\n" 
        p2 = roll(1, 20, qui["sagesse"] + qui["surprise"])
        return p1 + p2

    elif "!sommeil" in macro_text.lower():
        p1 = "Nombre de cibles touchées par le sort de sommeil d'Eustache :\n" 
        p2 = roll(1, 6, 3)
        return p1 + p2

#______Tests stats____________________________________________________________________
    
    elif "!stat" in macro_text.lower():
        return toutes_stat(qui, perso)

    elif len(macro_text) < 4:
        return short_dice(macro_text, perso, 1, 20)
    
    elif len(macro_text) == 4:
        return afficher_une_stat(qui, perso, macro_text, 1, 20)

    else:
        return "not a macro"

#_____________________________________________________________________________________


def macro_pyo_dm (macro_text) :
    if '!macro' in macro_text.lower():
        return "\n\n```!eustache```Affiche les macros pour Eustache."

    elif '!eustache' in macro_text.lower():
        text = [
        "\n\n```!i```lance !1d20 + i pour i valant de -9 à 99 sans signe + devant i."
        "\n\n```!carac```Affiche les macros concernant les caractéristiques d'Eustache."
        "\n\n```!armes```Affiche les macros concernant les armes d'Eustache."
        "\n\n```!voies```Affiche les macros concernant les voies d'Eustache."
        ]
        return text[0]

    elif '!carac' in macro_text.lower():
        text = [
        "\n\n```!stat```Affiche les caractéristiques d'Eustache."
        "\n\n```!for```Eustache teste sa force."
        "\n\n```!dex```Eustache teste sa dextérité."
        "\n\n```!con```Eustache teste sa constitution."
        "\n\n```!int```Eustache teste son intelligence."
        "\n\n```!sag```Eustache teste sa sagesse."
        "\n\n```!cha```Eustache teste son charisme."
        "\n\n```!surpise```Jet de perception d'Eustache en cas de surprise."
        ]
        return text[0]

    elif '!armes' in macro_text.lower():
        text = [
        "\n\n```!arbalète```Eustache tire à l'arbalète."
        "\n\n```!darbalète```Dégâts de l'arbalète d'Eustache.\n"

        "\n\n```!dague```Eustache donne un coup de dague."
        "\n\n```!ddague```Dégâts de la dague d'Eustache.\n"

        "\n\n```!lpierres```Eustache tire au lance-pierres."
        "\n\n```!dlpierres```Dégâts du lance-pierres d'Eustache.\n"

        "\n\n```!rapière```Eustache donne un coup de rapière."
        "\n\n```!dlpierres```Dégâts de la rapière d'Eustache.\n"
        ]
        return text[0]

    elif '!voies' in macro_text.lower():
        text = [
        "\n\n```!sort```Eustache lance un sort."
        "\n\n```!surpise```Jet de perception d'Eustache en cas de surprise."
        "\n\n```!sommeil```Nombre de cibles du sort de sommeil d'Eustache."
        ]
        return text[0]

    else:
        return "pas perso"