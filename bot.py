#!/usr/bin/python3.8
#coding:u8

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

import os
import discord

from commandes.all_cmd import *
from commandes.all_macro import *

from generation.generer_commanditaire import * # provisoire pour tester !quete.

class MyClient(discord.Client):

    async def on_ready(self):

        print(f'{self.user} est connectée à Discord !')
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="!help"))

    async def on_message(self, message):

        if ("!quete" in message.content): # pour tester !quete en le faisant tourner en boucle.
            if (message.author.name == "Jaenne") or (message.author == client.user):
                text = "\n!quete" + generer_commanditaire()
                if len(text) < 1950: # max discord text lenght = 2000.
                    await message.channel.send(text)
                else:
                    await message.channel.send("!quete")
                    print("testé")

        canal, text = is_it_macro(message, client)
        if text != "not a macro":
            await canal.send(text)
        else:
            canal, text = is_it_cmd(message, client)
            if text != "not a cmd":
                await canal.send(text)
                

client = MyClient()
client.run(XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX)


