from random import randrange

from generer.classe_personnage import Personnage

def comprendre_souhaits_utilisateur(message):
	"""
	Prend une commande utilisateur en argument.

	Appelle la classe Personnage.

	Appelle certaines fonction de la classe Personnage
	afin de générer un personage généré semi-aléatoirement 
	correspondant aux souhaits de l'utilisateur.

	Renvoie un texte décrivant le personnage.
	
	"""
	text = [""]
	perso = Personnage()

	perso.set_cmd_text(message)
	perso.set_type_de_personnage()
	
	text[0], cmd = perso.set_total_points_et_valeur_max()
	if not cmd :
		return text[0]
	
	perso.set_param_identite()
	perso.set_param_proscrits()
	perso.set_particularites()
	perso.bonus_de_metier()

	return perso.afficher_personnage()
