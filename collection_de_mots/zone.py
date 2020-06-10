"""
Les listes qui permettent de générer des lieux.

superficie
densite
activite
richesse 
climat
paysage
auberge_nom
auberge_adj
navire_nom 
navire_adj
lieu_discret
lieu_quete_nom
lieu_quete_adj
ext_nom
ext_adj
matiere_extraite 
chasse
magie
drogue
esclavage
religion
artisants
commercants
eleveurs 
alcool
rose_vent
quelle_zone
cosmopolite_ou_race
"""

superficie = [
	"très petite",
	"petite",
	"grande",
	"très grande",
	"immense",
	]

densite = [
	"déserte",
	"tranquille",
	"très peuplée",
	"surpeuplée",
	]

activite = [
	"le commerce",
	"l'esclavage",
	"la religion",
	"la magie",
	"la contrebande",
	"l'élevage",
	"la construction",
	"l'alcool",
	"la drogue",
	"la pêche",
	"la chasse",
	"l'agriculture",
	"l'artisanat",
	"l'extraction minière",
	]

richesse = [
	"misérable",
	"pauvre",
	"plutôt à l'aise financièrement",
	"riche",
	]

climat = [	
    "doux",
    "rude",
    "tempéré",
	]

paysage = [
	"une île",
	"une presqu'île",
	"bordée de montagnes",
	"à flanc de montagne",
	"un plateau",
	"sur une coline",
	"entourée de champs",
	"entourée de forêt",
	"au milieu d'un désert",
	"sur les bords de mer",
	"très boisée",
	"très rocheuse",
	"entourée de villes",
	"souterraine",
	"aérienne",
	"dans une vallée",
	"traversée par une rivière",
	"sur [d'anciens] des marécages",
	]

auberge_nom = [
	"Le sanglier",
	"Le cerf",
	"les trois p'tits chats",
	"La caille",
	"le porc",
	"l'ours",
	"l'enfant",
	"les marrons",
	"la citrouille",
	"la marraine",
	"l'étoile",
	"les poissons",
	"le pêcheur",
	"la chasseuse",
	"les oies",
	"les pommes de terres",
	"le boeuf",
	"la vache",
	"les faisans",
	"le merlu",
	"le chevreuil",
	"la chèvre",
	"les lapins",
	"le canard",
	"le fromage",
	"le festin",
	"la cuisse",
	"le mouton",
	"l'agneau",
	"le gigot",
	"le ragout",
	"la tourte",
	]

auberge_adj = [
	"rieur/rieuse.s",
	"chanceux/chanceuse.s",
	"colérique.s",
	"du roi",
	"de la reine",
	"gourmand.e.s",
	"joyeux/joyeuse.s",
	"rouge.s",
	"gentil.le.s",
	"chaud.e.s",
	"roux/rousse.s",
	"aillé.e.s",
	"roti.e.s",
	"gras.se.s",
	"faisandé.e.s",
	"barbu.e.s",
	"cendré.e.s",
	"fumé.e.s",
	"gargantuesque.s",
	"doré.e.s",
	"qui sent",
	"goutu.e.s",
	"aux pruneaux",
	"juteux/justeuse.s",
	"à l'ail",
	"piquant.e.s",
	"épicé.e.s",
	"crémeux/crémeuse.s",
	]

navire_nom = [
	"l'anguille",
	"la sirène",
	"le loup",
	"le lamentin",
	"le sabre",
	"le capitaine",
	"l'étoile",
	"le poisson",
	"l'équipage",
	"la sorcière",
	]

navire_adj = [
	"des mers",
	"intrépide",
	"chanceux/chanceuse",
	"sans peurs",
	"libre.s",
	"fier/fière",
	"valeureux/valeureuse",
	"volant.e",
	"sacré.e",
	"vert.e",
	"étincelant.e",
	]

lieu_discret = [
	"dans la forêt",
	"dans les égouts",
	"dans une grotte",
	"dans les docs",
	"sous le pont",
	]

lieu_quete_nom = [
	"le temple",
	"la tombe",
	"les cavernes",
	"le chateau",
	"la pyramide",
	"le couvent",
	"l'ancienne prison",
	"le donjon",
	"le labyrinthe",
	"l'antre",
	]

lieu_quete_adj = [
	"du roi maudit",
	"la reine rouge",
	"sombre.s",
	"hanté.e.s",
	"maudit.e.s",
	"du dragon blanc",
	]

ext_nom = [
	"la forêt",
	"la montagne",
	"l'île",
	"les plaines",
	"la vallée",
	"la jungle",
	"le verger",
	]

ext_adj = [
	"sombre.s",
	"sacré.e.s",
	"maudit.e.s",
	"vert.e.s",
	]

matiere_extraite = [
	"de quartz",
	"de fer",
	"d'acier",
	"d'airain",
	"de saphir",
	"de diamant",
	]

chasse = [
	"du Cerf blanc",
	"de Diane",
	]

magie = [
	"de la quintessence",
	"philosophale",
	"des érudit",
	"des illusions",
	]

drogue = [
	"des rêves embrumés",
	"des rêveurs",
	"des plaisirs",
	"paradis",
	"des mirages",
	]

esclavage = [
	"des enchaînés",
	"des entraves",
	]

religion = [
	"des éveillés",
	"des illuminés",
	"de la foi",
	]

artisants = [
	"des façonneurs",
	"de terre cuite",
	"aux milles éclats",
	"des forges rouges",
	"des alchimistes",
	"des miroirs",
	"des milles senteurs",
	]

commercants = [
	"des milles senteurs",
	"aux milles couleurs",
	"des merveilles",
	]

eleveurs = [
	"de la toison d'or",
	"de plumes",
	"des peaux",
	"des puces",
	]

alcool = [
	"de Bacchus",
	"dansante",
	"qui tangue"
	]

rose_vent = [
	"au nord",
	"à l'est",
	"au sud",
	"à l'ouest",
	"au nord-est",
	"au nord-ouest",
	"au sud-est",
	"au sud-ouest",
	]

quelle_zone = [
	"ici",
	"ailleurs",
	]

cosmopolite_ou_race = [
	"cosmopolite",
	]
