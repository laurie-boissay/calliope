"""
Toutes les commandes de Calliope qui ne sont pas des macro ;

+ la commande !macro qui donne accés aux macro ;
+ les réactions de Calliope aux critiques.

- les commandes de lancer de dés.
"""

import discord
from random import randrange

from commandes.des import *

from generation.generer_quete import *
from generation.generer_commanditaire import *
from generation.generer_nom import *
from generation.generer_pj import *

from collection_de_mots.calliope_reaction import *

def is_it_cmd(message, client):

    canal = message.channel
    text = "not a cmd"

    if (message.author == client.user): # User is Calliope.

        if message.channel.id == 692765037231603734 :
            text = reaction_crit(message.content)

        return canal, text
    
    else: # Other Users.

        if message.content.startswith('!'):
            text = all_users_cmd(message.content)
            if text != "not a cmd":
                canal = message.author
            else :
                text = commande_des(message.content)
                if text != "not a cmd" :
                    text = str(message.author.name) + " s'empare des dés : " + text

        elif 'calliope calliope calliope' in message.content.lower():
            canal = message.author
            text = ("https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Flarondepoetique.com%2Fwa_import187.jpg%3Fv%3D24zc2o6a5we22v1&f=1&nofb=1")

        return canal, text

def all_users_cmd(message):
    plus_de_quetes = [
    "!voler", "!infiltrer", "!protéger", "!livrer", "!enquêter",
    "!kidnaper", "!tuer", "!détruire", "!trouver", "!sauver",
    "!fabriquer", "!capturer", "!empoisonner", "!intercepter"
    ]

    if message.startswith('!help'):
        text = [
        "Je suis Calliope, la muse de la poésie épique et du jeu de rôle."
        "\nTu peux me parler en toute confidentialité en message privé."
        "\n\n```!quete```Génère une quête."
        "\n\n```!+quetes```Affiche les commandes pour choisir le type de quête."
        "\n\n```!zone```Génère une zone."
        "\n\n```!pnj```Génère un personnage."
        "\n\n```!auberge```Génère un nom d'auberge."
        "\n\n```!1d20-5   !1d20+5```Lance 1 dé 20 +/-5."
        "\n\n```!macro```Affiche les macros disponibles pour tes personnages."
        "\n\n```!info```La magie en oeuvre pour ma création."
        ]
        return text[0]

    elif message.startswith("!quete"):
        text = generer_commanditaire()
        if len(text) < 1950: # max discord text lenght = 2000.
            return text
        else :
            return all_users_cmd(message)

    elif message.startswith("!+quetes"):
        text = [
        "Voici les 14 types de quêtes :"
        "\n\n```!voler```"
        "\n```!infiltrer```"
        "\n```!protéger```"
        "\n```!livrer```"
        "\n```!enquêter```"
        "\n```!kidnaper```"
        "\n```!tuer```"
        "\n```!détruire```"
        "\n```!trouver```"
        "\n```!sauver```"
        "\n```!fabriquer```"
        "\n```!capturer```"
        "\n```!empoisonner```"
        "\n```!intercepter```"
        ]
        return text[0]

    elif message in plus_de_quetes:
        text = afficher_quete(message.strip("!"))
        if len(text) < 1950: # max discord text lenght = 2000.
            return text
        else :
            return all_users_cmd(message)

    elif message.startswith('!zone'):
        return "Bienvenue dans "+ zone()

    elif message.startswith('!pnj'):
        return "C'est "+ personne()

    elif message.startswith('!auberge'):
        return nom_auberge()

    elif message.startswith('!macro'):
        return "Tu n'as pas encore de macro.\nDemande à Jaenne pour en ajouter."

    elif message.startswith('!info'):
        text = [
        "Vous pensez que les gnomes ont le monopole de la technologie ?"
        "\nVous pouvez participer à mon amélioration :" 
        "\nhttps://github.com/laurie-boissay/calliope."
        ]
        return text[0]

    elif message.startswith('!pj'):
        return arguments_reroll(message)

    else:
        return "not a cmd"
    

def reaction_crit(message):

    if '(1)' in message:
        text = echec_crit[randrange(len(echec_crit))]

    elif '(20)' in message:
         text = reussite_crit[randrange(len(reussite_crit))]

    else:
        text = "not a cmd"

    return text
