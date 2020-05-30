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
from collection_de_mots.personnes import *

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

    if message.startswith('!help'):
        text = [
        "Je suis Calliope, la muse de la poésie épique et du jeu de rôle."
        "\nTu peux me parler en toute confidentialité en message privé."
        "\n\n```!quete```Génère une quête."
        "\n\n```!+quetes```Affiche les commandes pour choisir le type de quête."
        "\n\n```!zone```Génère une zone."
        "\n\n```!pnj```Génère un personnage."
        "\n\n```!personnage```Affiche les détais de la commande permettant de créer un PJ ou PNJ personnalisé."
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

    elif message.strip("!") in quete:
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

    elif message.startswith('!races'):
        text = "Vous pouvez choisir la race des :\n"
        for i in range(len(pers_race)):
            text += pers_race[i] + ", "
        return text

    elif message.startswith('!genres'):
        text = ""
        for i in range(len(pers_genre)):
            text += pers_genre[i] + ", "
        return text

    elif message.startswith('!métiers'):
        text = [
        "```!pj, 12, 3, métier=archer/archère```\n"
        "A noter que :"
        "```!pj, 12, 3, métier=archer/archère de la garde royale```"
        "Favorise aussi la caractéristique dextérité lors de la distribution des points de compétences.\n"
        '''Seul le premier mot sans espace après le signe = compte. Ici c'est "archer/archère".\n\n'''
        ]
        for k, v in metiers_et_carac_associee.items():
            text[0] += k + " : " + v + "\n"
        return text[0]

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

    elif message.startswith('!personnage'):
        text = [
        "\n\n```!pj, x, y```Génère un pj x et y sont obligatoires."
        "\nx correspond au points de caractéristiques à dépenser."
        "\ny correspond au maximum de points à dépenser dans une caractéristique."
        "\n```!pj, 12, 3```Exemple de PJ généré sans aucun paramètre facultatif."

        "\n\nTu peux préciser autant de paramètres facultatifs que tu le souhaites en les séparant chacun d'une virgule."
        "\nJe comblerait tous les paramètres laissés vides :"
        "\n```!pj, 12, 3, prénom=Toto, nom=du clan de Toto, race=orc, métier=mage, age=20, ville=Trifouillis les oies, genre=androgyne, secret=est violent```"

        "\n\n```!races```Affiche la liste des races qui influencent le choix du nom et du prénom."
        "\n\n```!genres```Affiche la liste des genres qui influencent le choix du nom et du prénom."
        "\n```!métiers```Affiche la liste des métiers qui favorisent une caractéristiques."
        ]
        return text[0]

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
