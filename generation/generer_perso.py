from random import randrange

from generation.classe_personnage import Personnage

def comprendre_souhaits_utilisateur(message):
	text = [""]
	perso = Personnage()

	perso.set_cmd_text(message)
	perso.set_type_de_personnage()
	
	text[0], cmd = perso.set_total_points_et_valeur_max()
	if not cmd :
		return text[0]
	
	perso.set_param_identite()
	perso.set_param_proscrits()
	perso.generer_particularites()
	perso.bonus_de_metier()

	return perso.afficher_personnage()
