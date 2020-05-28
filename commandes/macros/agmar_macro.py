"""
Les macro de MdJ de Agmar.

"""

from commandes.des import *
from commandes.caracteristiques import *

def macro_agmar (macro_text) :
    perso = "Le MdJ"

    if "!filtch" in macro_text.lower():
        return toutes_stat(carac_filtch, "Filtch")
        
    elif "!jaenne" in macro_text.lower():
        return toutes_stat(carac_jaenne, "Jaenne")

    elif "!willow" in macro_text.lower():
        return toutes_stat(carac_willow, "Willow")

    elif "!darius" in macro_text.lower():
        return toutes_stat(carac_darius, "Darius")

    elif "!duncan" in macro_text.lower():
        return toutes_stat(carac_duncan, "Duncan")
        
    elif len(macro_text) < 4:
        return perso + " saisit ses dés :" + short_w_of_d(macro_text)

    else:
        return "pas Agmar"


def macro_agmar_dm (macro_text) :
    if '!macro' in macro_text.lower():
        return "\n\n```!agmar```Affiche les macros pour Agmar."

    elif '!agmar' in macro_text.lower():
        text = [
        "\n\n```!'i'```lance !2d6 + i pour i valant de -9 à 99 sans signe + devant i."       
        "\n\n```!filtch```Affiche les caractéristiques de Filtch."
        "\n\n```!jaenne```Affiche les caractéristiques de Jaenne."
        "\n\n```!willow```Affiche les caractéristiques de Willow."
        "\n\n```!darius```Affiche les caractéristiques de Darius."
        "\n\n```!duncan```Affiche les caractéristiques de Duncan."
        ]
        return text[0]

    else:
        return "pas perso"



