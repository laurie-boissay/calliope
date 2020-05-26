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

        #_________Agmar___________________________________________________________________________

        if (message.author.name == "Agmar"):

            if message.content.startswith('!'):
                text = macro_agmar_dm(message.content)
                if text != "pas perso":
                    canal = message.author
                else :
                    text = macro_agmar(message.content)
        
        #_________Idaho___________________________________________________________________________
            
        elif (message.author.name == "Idaho"):

            if message.content.startswith('!'):
                text = macro_idaho_dm(message.content)
                if text != "pas perso":
                    canal = message.author
                else:
                    text = macro_gargrim(message.content)
                  
        #_________Jaenne_________________________________________________________________________

        elif (message.author.name == "Jaenne"): #"Jaenne"

            if message.content.startswith('!'):
                text = macro_jaenne_dm(message.content)
                if (text != "pas perso"):
                    canal = message.author
                else :
                    if (message.content.startswith('!dm')) or (message.content.startswith('!m')):
                        text = macro_merest(message.content)
                       
                    else:
                        text = macro_jaenne(message.content)
        #_________Lex_____________________________________________________________________________
            
        elif (message.author.name == "Lex"):

            if message.content.startswith('!'):
                text = macro_lex_dm(message.content)
                if text != "pas perso":
                    canal = message.author
                else:
                    text = macro_lex(message.content)
                    if text == "pas Lex":
                        text = macro_filtch(message.content)           
                        
        #_________Mel_____________________________________________________________________________
            
        elif (message.author.name == "Mel"):

            if message.content.startswith('!'):
                text = macro_mel_dm(message.content)
                if text != "pas perso":
                    canal = message.author
                else:
                    text = macro_willow(message.content)
                   
        #_________PYo_____________________________________________________________________________
            
        elif (message.author.name == "PYo"):

            if message.content.startswith('!'):
                text = macro_pyo_dm(message.content)
                if text != "pas perso":
                    canal = message.author
                else:
                    text = macro_eustache(message.content)
                    
        #_________Stevendeo_____________________________________________________________________________
            
        elif (message.author.name == "Stevendeo"):

            if message.content.startswith('!'):
                text = macro_stevendeo_dm(message.content)
                if text != "pas perso":
                    canal = message.author
                else:
                    text = macro_duncan(message.content)

        #_________tasneo_____________________________________________________________________________
            
        elif (message.author.name == "tasneo"):

            if message.content.startswith('!'):
                text = macro_tasneo_dm(message.content)
                if text != "pas perso":
                    canal = message.author
                else:
                    text = macro_darius(message.content)
          
        #__________________________________________________________________________________________

    return canal, text

