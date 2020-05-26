"""
Les macro de MdJ de Agmar.

"""

from commandes.des import *
from commandes.caracteristiques import *

def macro_agmar (macro_text) :
    perso = "Le MdJ"

    if "!filtch" in macro_text.lower():
        return stat_w_of_d(carac_filtch, "Filtch")
        
    elif "!jaenne" in macro_text.lower():
        return stat_w_of_d(carac_jaenne, "Jaenne")

    elif "!willow" in macro_text.lower():
        return stat_w_of_d(carac_willow, "Willow")

    elif "!darius" in macro_text.lower():
        return stat_w_of_d(carac_darius, "Darius")

    elif "!duncan" in macro_text.lower():
        return stat_w_of_d(carac_duncan, "Duncan")
        
    elif len(macro_text) < 4:
        return perso + " saisit ses dés :" + short_w_of_d(macro_text)

    else:
        return "pas Agmar"


def macro_agmar_dm (macro_text) :
    if '!macro' in macro_text.lower():
        text = "\n\n```!agmar```Affiche les macros pour Agmar."
        return text

    elif '!agmar' in macro_text.lower():
        text = ""
        macro_agmar = [
        "\n\n```!'i'``` Effectue !2d6 + 'i'"       
        "\n\n```!filtch```Affiche les caractéristiques de Filtch."
        "\n\n```!jaenne```Affiche les caractéristiques de Jaenne."
        "\n\n```!willow```Affiche les caractéristiques de Willow."
        "\n\n```!darius```Affiche les caractéristiques de Darius."
        "\n\n```!duncan```Affiche les caractéristiques de Duncan."
        ]

        for ligne in range(len(macro_agmar)):
            text += macro_agmar[ligne]
        return text

    else:
        return "pas perso"



