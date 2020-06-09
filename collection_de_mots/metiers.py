"""
Les listes + 1 dictionnaire permettant de générer des métiers/classes de personnages.

poste_palais_justice
poste_caserne
poste_capitainerie
poste_chateau
poste_guilde
poste_temple
pers_metier
metiers_et_carac_associee {}
classe_pers
carac
atouts_pj
	#meilleur_atout_archer.e
	#meilleur_atout_assassin
	#meilleur_atout_barbare
	#meilleur_atout_barde
	#meilleur_atout_druide
	#meilleur_atout_guerrière_guerrier
	#meilleur_atout_mage
	#meilleur_atout_moine
	#meilleur_atout_necromancien.ne
	#meilleur_atout_paladin.e
	#meilleur_atout_prêtre.sse
	#meilleur_atout_rodeur_rodeuse
	#meilleur_atout_sorcier_sorcière
	#meilleur_atout_voleur_voleuse
	#meilleur_atout_autre

pas_étudiant_e
"""


poste_palais_justice = [
	"juge",
	"avocat.e",
	"greffier/greffière",
	"garde",
	"procureur"
	]

poste_caserne = [
	"garde",
	"soldat",
	"sergent.e",
	"lieutenant.e",
	"capitaine",
	"commandant.e",
	"commissaire"
	]

poste_capitainerie =[
	"marin",
	"capitaine",
	"docker"
	]

poste_chateau = [
	"reine/roi",
	"ministre",
	"conseiller/conseillère",
	"soldat",
	"serviteur/servante",
	"soldat",
	"serviteur/servante",
	"soldat",
	"serviteur/servante",
	"soldat",
	"serviteur/servante",
	"cuisinier/cuisinière"
	]

poste_guilde = [
	"le chef",
	"le bras droit du chef",
	"simple membre",
	"simple membre",
	"simple membre",
	"simple membre",
	"simple membre",
	"simple membre",
	"simple membre"
	]

poste_temple =[
	"grand.e prêtre.sse",
	"moine",
	"copiste",
	"évèque",
	"moine",
	"moine",
	"moine",
	"moine",
	"moine",
	"moine",
	"moine"
	]

pers_metier = [
	"alchimiste",
	"apprenti.e",
	"artisan.ne",
	"archer/archère",
	"architecte",
	"assassin",
	"astrologue",
	"barde",
	"boulanger/boulangère",
	"bourreau",
	"capitaine",
	"cartographe",
	"chasseur/chasseuse",
	"chevalier/chevalière",
	"comédien.ne",
	"conseillère/conseiller royal.e",
	"contremaître",
	"courtisant/courtisanne",
	"couturier/couturière",
	"cuisinière/cuisinier",
	"duc/duchesse",
	"druide",
	"écuyère/écuyer",
	"écrivain.e publique/public",
	"éleveur/éleveuse",
	"étudiant.e",
	"forgeron.ne",
	"garde",
	"géographe",
	"guerrière/guerrier",
	"haut-placé.e",
	"joalière/joalier",
	"juge",
	"linguiste",
	"maçon.ne",
	"maire",
	"mage",
	"marchand.e",
	"maréchal.e ferrant.e",
	"marin",
	"médecin",
	"mendiant.e",
	"meunière/meunier",
	"mineur/mineuse",
	"nécromancien.ne",
	"ministre",
	"paladin.e",
	"paysan.ne",
	"pêcheur/pêcheuse",
	"peintre",
	"prefet",
	"prêtre.sse",
	"prince.sse",
	"professeur.e",
	"reine/roi",	
	"servante/serviteur",
	"serveur/serveuse",
	"sorcier/sorcière",
	"soldat.e",
	"tanneur/tanneuse",
	"tavernier/tavernière",
	"voleur/voleuse",
	]
	
metiers_et_carac_associee = {
	"alchimiste" : "Intelligence",
	"apprenti.e" : "Selon le métier étudié",
	"artisan.ne" : "Dextérité",
	"archer/archère" : "Dextérité",
	"architecte" : "Intelligence",
	"assassin" : "Dextérité",
	"astrologue" : "Sagesse",
	"barbare" : "Force",
	"barde" : "Charisme",
	#"boulanger/e" : ,
	"bourreau" : "Force",
	"capitaine" : "Sagesse",
	"cartographe" : "Intelligence",
	"chasseur/chasseuse" : "Dextérité",
	"chevalier/chevalière" : "Force",
	"comédien.ne" : "Charisme",
	"conseillère/conseiller" : "Sagesse",
	"contremaître" : "Sagesse",
	"couturier/couturière" : "Dextérité",
	"courtisant/courtisanne" : "Charisme",
	#"cuisinière/cuisinier" : ,
	"duc/duchesse" : "Charisme",
	"druide" : "Sagesse",
	"écuyère/écuyer" : "Constitution",
	"écrivain.e" : "Intelligence",
	"éleveur/éleveuse" : "Constitution",
	"étudiant.e" : "Selon le métier étudié",
	"forgeron.ne" : "Force",
	"garde" : "Force",
	"géographe" : "Intelligence",
	"guerrière/guerrier" : "Force",
	"haut-placé.e" : "Charisme",
	"joalière/joalier" : "Dextérité",
	"juge" : "Sagesse",
	"linguiste" : "Intelligence",
	"maçon.ne" : "Force",
	"maire" : "Charisme",
	"mage" : "Intelligence",
	"marchand.e" : "Charisme",
	"maréchal.e" : "Constitution",
	"marin" : "Constitution",
	"médecin" : "Intelligence",
	"mendiant.e" : "Constitution",
	#"meunière/meunier" : ,
	"mineur/mineuse" : "Force",
	"nécromancien.ne" : "Intelligence",
	"ministre" : "Charisme",
	"moine" : "Sagesse",
	"paladin.e" : "Charisme",
	"paysan.ne" : "Constitution",
	"pêcheur/pêcheuse" :"Constitution" ,
	"peintre" : "Sagesse",
	"prefet" : "Charisme",
	"prêtre.sse" : "Sagesse",
	"prince.sse" : "Charisme",
	"professeur.e" : "Intelligence",
	"reine/roi" : "Charisme",
	"rodeur/rodeuse" : "Dextérité",
	"servante/serviteur" : "Constitution",
	"serveur/serveuse" : "Constitution",
	"sorcier/sorcière" : "Intelligence",
	"soldat.e" : "Force",
	"tanneur/tanneuse" : "Constitution",
	"tavernier/tavernière" : "Sagesse",
	"voleur/voleuse" : "Dextérité",
	}

classe_pers = [
	"archer/archère", # 0
	"assassin", # 1
	"barbare", # 2
	"barde", # 3
	"druide", # 4
	"guerrière/guerrier", # 5
	"mage", # 6
	"moine", # 7
	"nécromancien.ne", # 8
	"paladin.e", # 9
	"prêtre.sse", # 10
	"rodeur/rodeuse", # 11
	"sorcier/sorcière", # 12
	"voleur/voleuse", # 13
	]

carac = [
	"Force",
	"Dextérité",
	"Constitution",
	"Intelligence",
	"Sagesse",
	"Charisme",
	]

atouts_pj = [
	#meilleur_atout_archer.e = 0
	[
	"la maîtrise de son arme de prédilection",
	"sa vue perçante",
	"sa cadence de tir",
	"sa capacité à trouver les points faibles de sa cible",
	"sa connaissance des champs de batailles",
	],

	#meilleur_atout_assassin = 1
	[
	"sa maîtrise des armes à distances",
	"sa maîtrise des petites armes blanches",
	"sa maîtrise des poisons",
	"sa connaissance des points vitaux",
	"sa capacité à passer inaperçu",
	],

	#meilleur_atout_barbare = 2
	[
	"sa force extraordinaire",
	"son arme fétiche",
	"sa résistance à la douleur",
	"sa rage au combat",
	"sa technique de combat brutale",
	],

	#meilleur_atout_barde = 3
	[
	"sa musique",
	"sa magnifique tenue en dentelle",
	"sa collection de déguisements",
	"sa maîtrise du combat à la rapière",
	"sa débrouillardise",
	],

	#meilleur_atout_druide = 4
	[
	"sa maîtrise des sorts de protection",
	"son compagnon animal",
	"son affinité avec les animaux",
	"sa capacité à survivre dans la nature",
	"son affinité avec les végétaux",
	],

	#meilleur_atout_guerrière_guerrier = 5 
	[
	"sa maîtrise du bouclier",
	"la maîtrise de son arme de prédilection",
	"sa résistance au combat",
	"sa technique de combat",
	"sa capacité d'adaptation en combat",
	],

	#meilleur_atout_mage = 6
	[
	"sa maîtrise des sorts d'altération de la matière",
	"sa maîtrise des sorts de combat",
	"sa maîtrise des sorts de bufs et de débufs",
	"sa maîtrise des sorts de protections",
	"sa maîtrise des sorts basiques mais très pratiques",
	],

	#meilleur_atout_moine = 7
	[
	"sa maîtrise des techniques de combat",
	"le combat à mains nues",
	"sa maîtrise de son esprit",
	"sa connaissance de l'anatomie",
	"sa maîtrise de son corps",
	],

	#meilleur_atout_necromancien.ne = 8
	[
	"sa maîtrise des sorts de démonologie",
	"sa maîtrise des sorts de mort",
	"sa maîtrise des sorts de pure nécromancie",
	"sa maîtrise des sorts du sang",
	"sa maîtrise des sorts de magie noire",
	],

	#meilleur_atout_paladin.e = 9
	[
	"sa monture",
	"sa foi",
	"sa condition de noble",
	"son héroïsme",
	"son esprit stratégique",
	],

	#meilleur_atout_prêtre.sse = 10
	[
	"sa foi",
	"de pouvoir bénir ami.e.s et objet.s",
	"la prière",
	"sa capacité à soigner",
	"la formulation de mots de protection",
	],

	#meilleur_atout_rodeur_rodeuse = 11
	[
	"sa maîtrise de l'arc",
	"son animal",
	"sa maîtrise des techniques de combat",
	"sa capacité à survivre en pleine nature",
	"sa connaissance de la nature",
	],

	#meilleur_atout_sorcier_sorcière = 12
	[
	"sa maîtrise des sorts d'air",
	"sa capacité de divination",
	"sa maîtrise des envoutements",
	"sa maîtrise des sorts d'illusion",
	"sa maîtrise des sorts d'invocation",
	],

	#meilleur_atout_voleur_voleuse = 13
	[
	"sa capacité à passer inaperçu",
	"sa technique de combat nerveuse",
	"son agilité féline",
	"son absence d'étique au combat",
	"sa technique de combat précise",
	],

	#meilleur_atout_autre = 14
	[
	"son carnet de contacts bien rempli",
	"un bijou de grande valeur, facile à revendre",
	"son animal de compagnie qui connait quelques tours",
	"son encyclopédie de voyage qui a réponse à tout",
	"la recette du thé revivifiant écrite sur un coin de page d'un vieux livre moisi",
	"une arme de grande qualité achetée à un vieux pouilleux"
	],
]

pas_étudiant_e = [
	"apprenti.e",
	"capitaine",
	"duc/duchesse",
	"écuyère/écuyer",
	"étudiant.e",
	"haut-placé.e",
	"maire",
	"mendiant.e",
	"ministre",
	"prince.sse",
	"reine/roi",

	"archer/archère",
	"assassin", 
	"barbare",
	"barde",
	"druide",
	"guerrière/guerrier",
	"mage",
	"moine",
	"nécromancien.ne",
	"paladin.e",
	"prêtre.sse",
	"rodeur/rodeuse",
	"sorcier/sorcière",
	"voleur/voleuse",
	]
	