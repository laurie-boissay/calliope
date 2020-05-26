"""
Les macro de MdJ de Lex ;
Les macro du personnage de Lex : Filtch.
"""

from commandes.des import *
from commandes.caracteristiques import *

def macro_filtch (macro_text) :
    perso = "Filtch"
    qui = carac_filtch
    hobbit = 1

    if "!stat" in macro_text.lower():
        return stat_w_of_d(qui, perso)

    elif len(macro_text) < 4:
        return perso + " saisit ses dés :" + short_w_of_d(macro_text)
    
    if "!dexh" in macro_text.lower():
        p1 = perso + " teste sa dextérité (avec le bonus de hobbit) :\n"
        p2 = roll(2, 6, qui["dextérité"] + hobbit)
        return p1 + p2

    elif "!inth" in macro_text.lower():
        p1 = perso + " teste son intelligence (avec le bonus de hobbit) :\n"
        p2 =roll(2, 6, qui["intelligence"] + hobbit)
        return p1 + p2

    elif "!forh" in macro_text.lower():
        p1 = perso + " teste sa force (avec le bonus de hobbit) :\n"
        p2 =roll(2, 6, qui["force"] + hobbit)
        return p1 + p2

    elif "!conh" in macro_text.lower():
        p1 = perso + " teste sa constitution (avec le bonus de hobbit) :\n"
        p2 =roll(2, 6, qui["constitution"] + hobbit)
        return p1 + p2

    elif "!sagh" in macro_text.lower():
        p1 = perso + " teste sa sagesse (avec le bonus de hobbit) :\n"
        p2 =roll(2, 6, qui["sagesse"] + hobbit)
        return p1 + p2

    elif "!chah" in macro_text.lower():
        p1 = perso + " teste son charisme (avec le bonus de hobbit) :\n"
        p2 =roll(2, 6, qui["charisme"] + hobbit)
        return p1 + p2

    else:
        text = afficher_une_stat(qui, perso, macro_text)
        return text


def macro_lex (macro_text) :    
    if "!mérest" in macro_text.lower():
        return toutes_stat(carac_merest, "Mérest")

    if "!gargrim" in macro_text.lower():
        return toutes_stat(carac_gargrim, "Gargrim")

    if "!eustache" in macro_text.lower():
        return toutes_stat(carac_eustache, "Eustache")

    else:
        return "pas Lex"

def macro_lex_dm (macro_text) :
    if '!macro' in macro_text.lower():
        p1 = "\n\n```!filtch```Affiche les macros pour Filtch."
        p2 = "\n\n```!lex```Affiche les macros pour Lex."
        return p1 + p2

    elif '!filtch' in macro_text.lower():
        text = ""
        macro_filtch = [
        "\n\n```!dex```Jet de dextérité."
        "\n\n```!dexh```Jet de dextérité avec le bonus de hobbit."
        "\n\n```!int```Jet d'intelligence."
        "\n\n```!inth```Jet d'intelligence avec le bonus de hobbit."
        "\n\n```!for```Jet de force."
        "\n\n```!forh```Jet de force avec le bonus de hobbit."
        "\n\n```!con```Jet de Constitution."
        "\n\n```!conh```Jet de Constitution avec le bonus de hobbit."
        "\n\n```!sag```Jet de Sagesse."
        "\n\n```!sagh```Jet de Sagesse avec le bonus de hobbit."
        "\n\n```!cha```Jet de Charisme."
        "\n\n```!chah```Jet de Charisme avec le bonus de hobbit."
        "\n\n```!stat```Affiche les caractéristiques."
        "\n\n```!i```Lance 2d6 + i"
        ]

        for ligne in range(len(macro_filtch)):
            text += macro_filtch[ligne]
        return text

    elif '!lex' in macro_text.lower():
        text = ""
        macro_lex = [
        "\n\n```!mérest```Affiche les caractéristiques de Mérest."
        "\n\n```!gargrim```Affiche les caractéristiques de Gargrim."
        "\n\n```!eustache```Affiche les caractéristiques de Eustache."
        ]

        for ligne in range(len(macro_lex)):
            text += macro_lex[ligne]
        return text

    else:
        return "pas perso"



