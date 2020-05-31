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


players = [
"Agmar", # 0
"Idaho", # 1
"Jaenne", # 2
"Lex", # 3
"Mel", # 4
"PYo", # 5
"Stevendeo", # 6
"tasneo", #7
]

players_macro = [ #liste de fonctions
macro_agmar_dm,
macro_idaho_dm,
macro_jaenne_dm,
macro_lex_dm,
macro_mel_dm,
macro_pyo_dm,
macro_stevendeo_dm,
macro_tasneo_dm,
]

characters_macro = [ #liste de fonctions
macro_agmar,
macro_gargrim,
macro_personnages_jaenne,
macro_filtch,
macro_willow,
macro_eustache,
macro_duncan,
macro_darius,
]


def is_it_macro(message, client):
    """
    Un canal réponse et un message par défaut sont définits.

    La fonction vérifie si l'auteur du message est dans la liste players.

    Si oui, la personne a dans la liste players_macro au même index que son
    pseudo dans la liste précédente, la fonction qui contient ses macros
    qui répondent en messages privés. Elle est associé au nom macro_nickname_dm

    Et dans la liste characters_macro, toujours au même indice, la fonction 
    qui contient ses macros qui répondent dans le canal ou a été écrit le message. 
    Elle est associée au nom macro_personnage

    On regarde si le message commence par : !
    Si oui, on appelle macro_nickname_dm

    Et selon la réponse de cette fonction, soit le canal de réponse et le texte 
    sont modifiés soit la fonction macro_personnage est appelée. A son tour, elle
    modifie le texte.

    Dans tous les cas, le canal de réponse et le text sont renvoyés.
    """

    canal = message.channel
    text = "not a macro"

    #macro_nickname_dm = players_macro[7] # teste les macro d'autres utilisateurs.
    #macro_personnage = characters_macro[7] # teste les macro des perso d'autres utilisateurs.

  
    for i in range(len(players)):
        if message.author.name == players[i]:
            macro_nickname_dm = players_macro[i] 
            macro_personnage = characters_macro[i]
   
    if message.content.startswith('!'):
        text = macro_nickname_dm(message.content)
        if text != "pas perso":
            canal = message.author
        else :
            text = macro_personnage(message.content)
    
    return canal, text