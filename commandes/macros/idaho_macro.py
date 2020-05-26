"""
Les macros du personnage de Idaho : Gargrim.
"""

from commandes.des import *
from commandes.caracteristiques import *


def macro_gargrim (macro_text) :
    perso = "Gargrim"
    qui = carac_gargrim
    gantelets = 2
    maitre_arme = 1

    if "!hacheg" in macro_text.lower():
        p1 = "Gargrim donne un coup de hache de guerre (avec ses gantelets + maître d'arme) :\n" 
        p2 = roll(1, 20, carac_gargrim("force") + carac_gargrim("niveau") + maitre_arme + gantelets) 
        return p1 + p2

    elif "!couteaug" in macro_text.lower():
        p1 = "Gargrim donne un coup couteau (avec ses gantelets) :\n" 
        p2 = roll(1, 20, carac_gargrim("force") + carac_gargrim("niveau") + gantelets) 
        return p1 + p2

    elif "!hache" in macro_text.lower():
        p1 = "Gargrim donne un coup de hache de guerre (maître d'arme) :\n" 
        p2 = roll(1, 20, carac_gargrim("force") + carac_gargrim("niveau") + maitre_arme) 
        return p1 + p2

    elif "!couteau" in macro_text.lower():
        p1 = "Gargrim donne un coup de couteau :\n" 
        p2 = roll(1, 20, carac_gargrim("force") + carac_gargrim("niveau")) 
        return p1 + p2

    elif "!jet" in macro_text.lower():
        p1 = "Gargrim envoie sa hache de jet :\n" 
        p2 = roll(1, 20, carac_gargrim("dextérité") + carac_gargrim("niveau")) 
        return p1 + p2

    elif "!arbalète" in macro_text.lower():
        p1 = "Gargrim tire à l'arbalète :\n" 
        p2 = roll(1, 20, carac_gargrim("dextérité") + carac_gargrim("niveau")) 
        return p1 + p2

#______Dégâts____________________________________________________________________

    elif "!dhacheg" in macro_text.lower():
        p1 = "Dégâts de la hache de guerre de Gargrim (avec ses gantelets) :\n" 
        p2 = roll(1, 8, carac_gargrim("force") + gantelets) 
        return p1 + p2

    elif "!dcouteaug" in macro_text.lower():
        p1 = "Dégâts du couteau de Gargrim (avec ses gantelets) :\n" 
        p2 = roll(1, 6, carac_gargrim("force") + gantelets) 
        return p1 + p2

    elif "!dhache" in macro_text.lower():
        p1 = "Dégâts de la hache de guerre Gargrim :\n" 
        p2 = roll(1, 8, carac_gargrim("force")) 
        return p1 + p2

    elif "!dcouteau" in macro_text.lower():
        p1 = "Dégâts du couteau de Gargrim :\n" 
        p2 = roll(1, 6, carac_gargrim("force")) 
        return p1 + p2

    elif "!djetg" in macro_text.lower():
        p1 = "Dégâts de la hache de jet de Gargrim (avec ses gantelets) :\n" 
        p2 = roll(1, 6, carac_gargrim("force") + gantelets) 
        return p1 + p2

    elif "!djet" in macro_text.lower():
        p1 = "Dégâts de la hache de jet de Gargrim:\n" 
        p2 = roll(1, 6, carac_gargrim("force")) 
        return p1 + p2

    elif "!darbalète" in macro_text.lower():
        p1 = "Dégâts de l'arbalète de Gargrim :\n" 
        p2 = roll(3, 4, 0) 
        return p1 + p2

#______Tests stats____________________________________________________________________
    
    elif "!stat" in macro_text.lower():
        return stat_c_o(qui, perso)

    elif "!forg" in macro_text.lower():
        p1 = "Gargrim teste sa force (avec ses gantelets) :\n" 
        p2 = roll(1, 20, carac_gargrim("force") + gantelets) 
        return p1 + p2

#________voies_______________________________________________________________________

    elif "!absg" in macro_text.lower():
        p1 = "Gargrim absorbe un coup (avec ses gantelets) :\n" 
        p2 = roll(1, 20, carac_gargrim("force") + carac_gargrim("force") + gantelets)
        return p1 + p2

    elif "!abs" in macro_text.lower():
        p1 = "Gargrim absorbe un coup :\n" 
        p2 = roll(1, 20, carac_gargrim("force") + carac_gargrim("force"))
        return p1 + p2

    elif "!abssort" in macro_text.lower():
        p1 = "Gargrim absorbe un sort :\n" 
        p2 = roll(1, 20, carac_gargrim("sagesse"))
        return p1 + p2

#_____________________________________________________________________________________

    elif len(macro_text) < 4:
        return perso + " saisit ses dés :" + short_c_o(macro_text)
    
    else:
        text = afficher_1_stat(qui, perso, macro_text)
        return text

def macro_idaho_dm (macro_text) :
    if '!macro' in macro_text.lower():
        p1 = "\n\n```!gargrim```Affiche les macros pour Gargrim."
        return p1

    elif '!gargrim' in macro_text.lower():
        text = ""
        macro_gargrim = [
        "\n\n```!i```Lance !1d20 + i"
        "\n\n```!carac```Affiche les macros concernant les caractéristiques de Gargrim."
        "\n\n```!armes```Affiche les macros concernant les armes de Gargrim."
        "\n\n```!voies```Affiche les macros concernant les voies de Gargrim."
        ]

        for ligne in range(len(macro_gargrim)):
            text += macro_gargrim[ligne]
        return text

    elif '!carac' in macro_text.lower():
        text = ""
        macro_gargrim = [
        "\n\n```!stat```Affiche les caractéristiques de Gargrim."
        "\n\n```!ini```Affiche l'initiative de Gargrim."
        "\n\n```!déf```Affiche la défense de Gargrim."
        "\n\n```!forg```Gargrim teste sa force (avec ses gantelets)."
        "\n\n```!for```Gargrim teste sa force."
        "\n\n```!dex```Gargrim teste sa dextérité."
        "\n\n```!con```Gargrim teste sa constitution."
        "\n\n```!int```Gargrim teste son intelligence."
        "\n\n```!sag```Gargrim teste sa sagesse."
        "\n\n```!cha```Gargrim teste son charisme."
        ]

        for ligne in range(len(macro_gargrim)):
            text += macro_gargrim[ligne]
        return text

    elif '!armes' in macro_text.lower():
        text = ""
        macro_gargrim = [
        "\n\n```!hacheg```Gargrim donne un coup de hache de guerre (avec ses gantelets)."
        "\n\n```!dhacheg```Dégâts de la hache de guerre de Gargrim (avec ses gantelets).\n"
        
        "\n\n```!hache```Gargrim donne un coup de hache de guerre."
        "\n\n```!dhache```Dégâts de la hache de guerre de Gargrim.\n"
        
        "\n\n```!couteaug```Gargrim donne un coup couteau (avec ses gantelets)."
        "\n\n```!dcouteaug```Dégâts du couteau de Gargrim (avec ses gantelets).\n"
        
        "\n\n```!couteau```Gargrim donne un coup couteau."        
        "\n\n```!dcouteau```Dégâts du couteau de Gargrim.\n"

        
        "\n\n```!jet```Gargrim envoie sa hache de jet."
        "\n\n```!djetg```Dégâts de la hache de jet de Gargrim (avec ses gantelets)."
        "\n\n```!djet```Dégâts de la hache de jet de Gargrim.\n"

        "\n\n```!arbalète```Gargrim tire à l'arbalète."
        "\n\n```!darbalète```Dégâts de l'arbalète de Gargrim."
        ]
        for ligne in range(len(macro_gargrim)):
            text += macro_gargrim[ligne]
        return text

    elif '!voies' in macro_text.lower():
        text = ""
        macro_gargrim = [        
        "\n\n```!absg```Gargrim absorbe un coup (avec ses gantelets)."
        "\n\n```!abs```Gargrim absorbe un coup."
        "\n\n```!abssort```Gargrim absorbe un sort."
        ]

        for ligne in range(len(macro_gargrim)):
            text += macro_gargrim[ligne]
        return text

    else:
        return "pas perso"