"""
Toutes les macro des joueurs de mon serveur.
"""

import discord

from commandes.des import *

from commandes.macros.jaenne_macro import *
from commandes.macros.lex_macro import *
from commandes.macros.agmar_macro import *
from commandes.macros.idaho_macro import *
from commandes.macros.pyo_macro import *
from commandes.macros.mel_macro import *
from commandes.macros.stevendeo_macro import *
from commandes.macros.tasneo_macro import *


def is_it_macro(message, client):
    canal = message.channel
    text = "not a macro"

    if (message.author != client.user):

        if (message.author.name == "Agmar"):
            canal, text = is_it_a_macro_for_nickname(message, macro_agmar_dm, macro_agmar)
            
        elif (message.author.name == "Idaho"):
            canal, text = is_it_a_macro_for_nickname(message, macro_idaho_dm, macro_gargrim)

        elif (message.author.name == "Jaenne"): #"Jaenne"
            canal, text = is_it_a_macro_for_nickname(message, macro_jaenne_dm, macro_personnages_jaenne)
    
        elif (message.author.name == "Lex"):
            canal, text = is_it_a_macro_for_nickname(message, macro_lex_dm, macro_filtch)
            
        elif (message.author.name == "Mel"):
            canal, text = is_it_a_macro_for_nickname(message, macro_mel_dm, macro_willow)
            
        elif (message.author.name == "PYo"):
            canal, text = is_it_a_macro_for_nickname(message, macro_pyo_dm, macro_eustache)
            
        elif (message.author.name == "Stevendeo"):
            canal, text = is_it_a_macro_for_nickname(message, macro_stevendeo_dm, macro_duncan)

        elif (message.author.name == "tasneo"):
            canal, text = is_it_a_macro_for_nickname(message, macro_tasneo_dm, macro_darius)
          
    return canal, text

def is_it_a_macro_for_nickname(message, macro_nickname_dm, macro_personnage):
    canal = message.channel
    text = "not a macro"
    if message.content.startswith('!'):
        text = macro_nickname_dm(message.content)
        if text != "pas perso":
            canal = message.author
        else :
            text = macro_personnage(message.content)
    return canal, text