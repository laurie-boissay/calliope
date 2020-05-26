"""
Les commandes et macro de lancer de dés.
"""

from random import randint

def roll(nb_des, valeur_des, bonus):
    resultats = [0] * nb_des
    total = 0
    text = "\n" + str(nb_des) + " dé(s) " + str(valeur_des) + " :\n "

    for de in range(nb_des):
        resultats[de] = randint(1, valeur_des)
    for index in range(nb_des):
        text +=  str(resultats[index])
        total += resultats[index]
        if index != nb_des - 1 :
            text += " + "
    text = text + "\n (" + str(total) + ")" 
    if bonus != 0:
        text += " + son bonus/malus de " + str(bonus)
    text = text + " = " + "**" + str(total+bonus) + "**"
    return text

def commande_des(cmd):
    elements = list(cmd.strip("!"))
    nb_des = ""
    valeur_des = ""
    operateur = ""
    bonus = ""
    op = len(elements)
    
    for i in range(len(elements)):
        if elements[i] == "d":
            d = i
    for i in range(len(elements)):
        if elements[i] == "-":
            operateur = "-"
            op = i
    for i in range(len(elements)):
        if elements[i] == "+":
            operateur = "+"
            op = i

    for i in range(d):
        nb_des += elements[i]

    for i in range(op):
        if i > d:
            valeur_des += elements[i]
            
    for i in range(len(elements)):
        if i > op:
            bonus += elements[i]

    try :
        nb_des = int(nb_des)
        valeur_des = int(valeur_des)
        if bonus != "":
            bonus = int(bonus)
        else:
            bonus = 0

    except ValueError:
        return "\net se foule le poignet ?\nPour lancer 1 dé 20 avec un bonus de 5 : ```!1d20+5```"

    if operateur == "-":
        bonus *= -1

    return roll(nb_des, valeur_des, bonus)

def short_w_of_d(bonus):
    bonus = bonus.strip("!")
    text = "\net se foule le poignet ?\n!i fonctionne pour i valant de -1 à +5 inclus"

    try:
        bonus = int(bonus)
    except ValueError:
         return text

    if (bonus >= 6) or (bonus < -1):
        return text
    else:
        for i in range(-1, 6):
            if bonus == i:
                return roll(2, 6, bonus)

def short_c_o(bonus):
    bonus = bonus.strip("!")
    text = "\net se foule le poignet ?\n!i fonctionne pour i valant de -1 à +20 inclus"

    try:
        bonus = int(bonus)
    except ValueError:
         return text

    if (bonus >= 21) or (bonus < -1):
        return text
    else:
        for i in range(-1, 21):
            if bonus == i:
                return roll(1, 20, bonus)