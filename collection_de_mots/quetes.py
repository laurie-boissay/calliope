"""
Les listes qui servent à générer des mots pour varier le style des quêtes :
quete[]
quetes_illegales[]
recompense[]
recompense_de_quete[]
infiltration[]
protection[]
commanditaire[]
raison_inf[]
enquete[]
livraison[]
quantite[]
lieu_crime[]
destruction[]
interception[]
poison[]
menace_personne[]
menace_objet_perso[]
menace_lieu[]
quetes_caserne[]
commanditaires_enqueter_meurtre[]
mobile[]
description_scene[]
kid[]
kill[]
contexte_quetes_illegales[] 
contexte_quetes_legales[]

"""
from generer.nom import *

quete = [
	"voler",
	"infiltrer",
	"protéger",
	"livrer",
	"enquêter",
	"kidnaper",
	"tuer",
	"détruire",
	"trouver",
	"sauver",
	"fabriquer",
	"capturer",
	"intercepter",
	"empoisonner"
	]

quetes_illegales = [
	"voler",
	"kidnaper",
	"tuer",
	"détruire",
	"capturer",
	"empoisonner",
	]

recompense = [
	"un titre",
	"de l'argent",
	"une autorisation d'accès",
	"de l'or",
	"des bijoux",
	"un objet précieux",
	"le recrutement",
	"des terres"
	]

recompense_de_quete = [
	"de l'argent",
	"des bijoux",
	]

infiltration = [
	"un réseau",
	"une organisation"
	]

protection = [
	"une personne",
	"un secret",
	"un lieu",
	"un objet personnel",
	"un convoi"
	]

commanditaire = [
	"une organisation",
	"une personne",
	"un réseau"
	]

raison_inf = [
	"voler",
	"protéger",
	"libérer",
	"tuer",	
	"détruire",
	"sauver"
	]

enquete = [
	"un meurtre",
	"un kidnaping",
	"une organisation",
	"une personne",
	"un vol",
	"un réseau"
	]

livraison = [
	"une personne",
	"un objet personnel",
	"un animal",
	"un objet",
	"un animal",
	"de l'argent",
	"une caisse"
	]

quantite = [
	"faible quantité",
	"très grande quantité",
	"petite quantité",
	"quantité très importante"
	]

lieu_crime = [
	"lieu discret",
	"une organisation",
	"une maison"
	]

destruction = [
	"un objet",
	"une organisation",
	"un réseau",
	"un bâtiment"
	]

interception = [
	"des documents sensibles",
	"une lettre",
	"un convoi"
	]

poison = [
	"des caisses de nourriture",
	"le puit d'un village",
	"une personne",
	"un animal domestique"
	]

menace_personne = [
	"meurtre",
	"kidnaping"
	]

menace_objet_perso = [
	"le vol",
	"la destruction"
	]
menace_lieu =[
	"la destruction",
	"le pillage",
	"la prise de contrôle"
	]

quetes_caserne = [
	"tuer",
	"capturer",
	"intercepter",
	"protéger",
	"sauver",
	"infiltrer",
	"enquêter"
	]

commanditaires_enqueter_meurtre = [
	"le temple",
	"la caserne",
	"le chateau",
	]

mobile = [
	"la jalousie",
	"l'amour",
	"un cambriolage qui a mal tourné",
	"l'extortion d'informations",
	"la politique",
	"la vengence",
	"le chantage",
	"une prime sur la tête de la victime",
	"l'argent"
	]

description_scene = [
	"Tous les os de la victime sont brisés",
	"La tête de la victime n'est pas là",
	"La peau de la victime a pris une teinte bleue qui ne semble pas naturelle",
	"Il y a une trace de piqure sur la victime",
	"Le corps est calciné mais il n'y a pas de traces de brulure autour de lui",
	"La victime a de nombreuses traces de morsures sur le corps",
	"La victime a la bouche ouverte. Elle semble chercher son soufle, les mains sur la gorge",
	"Le sang de la victime tapisse le sol. L'arme du crime est à quelques mètres dissimulée par la pagaille ambiante",
	"La victime a le crâne fracassé"
	]

kid = [
	"personne",
	"animal"
	]

kill = [
	"personne",
	"animal",
	"monstre",
	"animal sauvage"
	]

contexte_quetes_illegales = [
	"Pst",
	"personne ivre",
	"lettre",
	"garçon",
	"fille",
	"mendiant.e",
	"contact",
] 

contexte_quetes_legales = [
	"annonce",
	"accosté.e.s",
	"tavernier.e",
] 