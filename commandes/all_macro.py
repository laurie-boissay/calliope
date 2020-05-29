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
"Agmar",
"Idaho",
"Jaenne",
"Lex",
"Mel",
"PYo",
"Stevendeo",
"tasneo",
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
    canal = message.channel
    text = "not a macro"

    for i in range(len(players)):
        if message.author.name == players[i]:
            canal, text = is_it_a_macro_for_nickname(message, players_macro[i], characters_macro[i])
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