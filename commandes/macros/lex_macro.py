"""
Les macro de MdJ de Lex.
"""

from commandes.des import *
from commandes.caracteristiques import *


def macro_lex (macro_text):
    perso = "Lex"   
    if "!mérest" in macro_text.lower():
        return toutes_stat(carac_merest, "Mérest")

    elif "!gargrim" in macro_text.lower():
        return toutes_stat(carac_gargrim, "Gargrim")

    elif "!eustache" in macro_text.lower():
        return toutes_stat(carac_eustache, "Eustache")

    elif len(macro_text) < 4:
        return short_dice(macro_text, perso, 1, 20)

    else:
        return "not a macro"

def macro_lex_dm (macro_text):
    if '!macro' in macro_text.lower():
        text = [
        "\n\n```!lex```Affiche les macros pour Lex."
        ]
        return text[0]

    elif '!lex' in macro_text.lower():
        text = [
        "\n\n```!mérest```Affiche les caractéristiques de Mérest."
        "\n\n```!gargrim```Affiche les caractéristiques de Gargrim."
        "\n\n```!eustache```Affiche les caractéristiques de Eustache."
        ]
        return text[0]

    else:
        return "pas perso"



