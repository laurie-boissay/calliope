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
    """
    Un canal de réponse et un texte sont définits par défaut.

    Vérifie si Calliope est l'auteur du message. Si oui, vérifie
    si le canal du message est le canal "JDR" de mon serveur Discord.

        Dans ce cas, appelle la fonction reaction_crit qui va modifier
        le texte.

    Si Calliope n'est pas l'auteur du message :

        Vérifie si le message commence par : !
            si oui, appelle all_users_cmd et selon sa réponse, modifie
            le text et le canal réponse ou appelle commande_des

                Modifie le texte selon la réponse de commande_des

        Vérifie si le message contient 'calliope calliope calliope'
            si oui, modifie le texte et le canal réponse.

    Dans tous les cas renvoit le canal réponse et le texte.

    """

    canal = message.channel
    text = "not a cmd"

    if (message.author == client.user): # User is Calliope.

        if message.channel.id == 692765037231603734 :
            text = reaction_crit(message.content)
    
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
    """
    Vérifie si le message commence par (ou contient) une commande.
        
        La majorité des commandes définissent simplement un texte.
        
        D'autres commandes définissent un texte, vérifient sa longueur
        et peuvent boucler sur elles mêmes si le texte est trop long.

        Et enfin certaines commandes appellent une fonction.

    Dans tous les cas, renvoit un texte.   

    """

    if message.startswith('!help'): 
        # Renvoi un message d'aide.
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
        # Appelle la fonction generer_commanditaire et vérifie la longueur
        # du texte reçu puis renvoi le texte ou boucle sur la fonction.
        text = generer_commanditaire()
        if len(text) < 1950: # max discord text lenght = 2000.
            return text
        else :
            return all_users_cmd(message)

    elif message.startswith("!+quetes"):
        # Renvoi les commandes pour choisir un type de quete.
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
        # Appelle la fonction afficher_quete et vérifie la longueur
        # du texte reçu puis renvoi le texte ou boucle sur la fonction.
        text = afficher_quete(message.strip("!"))
        if len(text) < 1950: # max discord text lenght = 2000.
            return text
        else :
            return all_users_cmd(message)

    elif message.startswith('!zone'):
        # Appelle la fonction qui génère une zone et renvoi un texte.
        return "Bienvenue dans "+ zone()

    elif message.startswith('!pnj'): 
        # Appelle la fonction qui génère un PNJ et renvoi un texte.
        return "C'est "+ personne()

    elif message.startswith('!auberge'): 
        # Appelle la fonction qui génère un nom d'auberge et renvoi un texte.
        return nom_auberge()

    elif message.startswith('!races'):
        # Renvoi la liste des races qui influencent la génération d'un patronyme
        # avec la commande !pj, x, y
        text = "Vous pouvez choisir la race des :\n"
        for i in range(len(pers_race)):
            text += pers_race[i] + ", "
        return text

    elif message.startswith('!genres'):
        # Renvoi la liste des genres qui influencent la génération d'un patronyme
        # avec la commande !pj, x, y
        text = ""
        for i in range(len(pers_genre)):
            text += pers_genre[i] + ", "
        return text

    elif message.startswith('!métiers'):
        # Renvoi la liste des métiers qui influencent la génération d'un personnage joueur
        # et une aide à l'utilisation de la commande !pj, x, y
        text = [
        "Enlever un ou plusieurs métier de la liste :"
        "```!pj, 12, 3, métier_bourreau, métier_contremaître```\n"

        "Choisir un métier qui a une caractéristique prioritaire :"
        "```!pj, 12, 3, métier=archer/archère```"
        "A noter que :"
        "```!pj, 12, 3, métier=archer/archère de la garde royale```"
        "Favorise aussi la caractéristique dextérité lors de la distribution des points de compétences.\n"
        '''Seul le premier mot sans espace après le signe = compte. Ici c'est "archer/archère".\n\n'''

        ]
        for k, v in metiers_et_carac_associee.items():
            text[0] += k + " : " + v + "\n"
        return text[0]

    elif message.startswith('!macro'):
        # La commande !macro est une macro si un utilisateur ayant tapé !macro
        # n'a pas de macro enregistrées, renvoi ce message :
        return "Tu n'as pas encore de macro.\nDemande à Jaenne pour en ajouter."

    elif message.startswith('!info'):
        # Renvoi le lien vers mon Github.
        text = [
        "Vous pensez que les gnomes ont le monopole de la technologie ?"
        "\nVous pouvez participer à mon amélioration :" 
        "\nhttps://github.com/laurie-boissay/calliope."
        ]
        return text[0]

    elif message.startswith('!pj'):
        # Appelle la fonction arguments_reroll, renvoi un texte.
        return arguments_reroll(message)

    elif message.startswith('!personnage'):
        # Renvoi le texte d'aide pour utiliser la commande !pj, x, y
        text = [
        "\n\n```!pj, x, y```Génère un pj x et y sont obligatoires."
        "\nx correspond au points de caractéristiques à dépenser."
        "\ny correspond au maximum de points à dépenser dans une caractéristique."
        "\n```!pj, 12, 3```Exemple de PJ généré sans aucun paramètre facultatif."

        "\n\nTu peux préciser autant de paramètres facultatifs que tu le souhaites en les séparant chacun d'une virgule."
        "\nJe comblerait tous les paramètres laissés vides :"
        "\n```!pj, 12, 3, prénom=Toto, nom=du clan de Toto, race=orc, métier=mage, age=20, leitmotiv=Apprendre pleins de blagues., ville=Trifouillis les oies, genre=androgyne, secret=est violent```"

        "\n\nTu peux aussi supprimer certaines valeurs de la liste des paramètres  :"
        "```!pj, 8, 2, prénom=Toto, race_elfe, race_demi-elfe, genre_féminin```"
        "Fonctionne pour : ```race_xxxx, métier_xxxx, genre_xxxx```"

        "\n\n```!races```Affiche la liste des races qui influencent le choix du nom et du prénom."
        "\n```!genres```Affiche la liste des genres qui influencent le choix du nom et du prénom."
        "\n```!métiers```Affiche la liste des métiers qui favorisent une caractéristiques."
        ]
        return text[0]

    else:
        return "not a cmd"
    

def reaction_crit(message):
    """
    Calliope va réagir messages contenant (1) ou (20).

    Renvoi un text.
    """

    if '(1)' in message:
        text = echec_crit[randrange(len(echec_crit))]

    elif '(20)' in message:
         text = reussite_crit[randrange(len(reussite_crit))]

    else:
        text = "not a cmd"

    return text
