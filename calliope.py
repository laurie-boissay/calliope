#!/usr/bin/python3.8
#coding:u8


#import os
import discord

from commandes.all_cmd import *
from commandes.all_macro import *


"""
Calliope est un robot discord pour le Jeu de rôle.
                            !help

Elle peut générer :
    - des quetes            !quete
    - des zones             !zone
    - des PNJ               !pnj
    - des noms d'auberges   !bar

Elle permet aux joueurs de lancer des dés.
                            !2d6-1
                            !1d20+5

Elle propose des macro pour les joueurs de mon serveur Discord
pour deux JDR différents.
                            !macro
"""


class MyClient(discord.Client):
    """
    Confirme dans la console que Calliope est connectée.

    Calliope affiche : "Regarde !help" sous son nom.

    Prend tous les message en entrée pour vérifier s'il s'agit d'une macro
    ou d'une commande.

    Appelle is_it_macro et selon sa réponse affiche le text dans le canal définit
    ou appelle la fonction is_it_cmd. 

    Selon la réponse de is_it_cmd, affiche le text dans le canal définit 
    ou ne fait rien.
    """
    async def on_ready(self):

        print(f'{self.user} est connectée à Discord !')
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="!help"))

    async def on_message(self, message):

        canal, text = is_it_macro(message, client)
        if text != "not a macro":
            await canal.send(text)
        else:
            canal, text = is_it_cmd(message, client)
            if text != "not a cmd":
                await canal.send(text)
                

client = MyClient()
client.run('SECRET TOKEN')


'''
TypeError: __new__() got an unexpected keyword argument 'deny_new' :
python3 -m pip install -U discord.py
'''



# cd /home/jaenne/Python/calliope
# ./calliope.py