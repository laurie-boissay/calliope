# Calliope est un robot discord en français pour le JDR.

La fonction de base est la génération de quêtes aléatoires pour servir d'inspiration à un Maître du Jeu.

D'autres fonctions ont été ajoutées ensuite :
  - la génération de zones
  - la génération de PNJ
  - La génération de noms d'auberges

Il s'agit de fonctions déjà utilisées par la génération de quêtes mais rendues accessibles séparément.

Puis j'ai eu envie de donner une interface à ce programme. C'est à ce moment que nous nous sommes tous confinés à cause de la pandémie de covid. Les différentes parties de jeux de rôles que nous avions en cours ont migrées tout naturellement vers mon serveur Discord. C'est la que Calliope devient un bot Discord. 

J'installe sur mon sereur Discord deux robots pour lancer les dés. Le plus utilisé par les joueurs de JDR est DiceParser.

Pour que mes amis s'intéressent à Calliope sans que je leur révèle qu'elle est ma création, je lui implémente des réactions aux résultats des deux autres robots en cas de réussite critique (20 sur le dé) ou échec critique (1 sur le dé). 

Puis je me dis qu'elle devrait faire des choses plus utiles et simplifier les commandes que nous utilisons. J'ai commencé par lui faire lancer DiceParser : le joueur ou la joueuse pouvait entrer une macro personnalisé de type !arc pour que Calliope réponde !2d6+2 par exemple et lance ainsi une réaction avec DiceParser qui répondait à son tour en "lançant les dés".

Les inconvéniants de cette méthode était la lisibilité et le bruit (dans les deux sens du terme) : pour obtenir 1 lancé de dé, 3 messages étaient affichés à l'écran et leur 3 alertes sonores retentissaient pour les autres joueurs. 

De plus si tous les joueurs executaient la même commande en même temps, il était plus compliqué de se mettre d'accord sur quel résultat appartenait à quel joueur. ex "Lancez tous 1 dé 6 pour voir combien de points de vie vous regagnez."

Calliope s'est alors mise à lancer les dés elle aussi. Elle identifie la personne ou le personnage qui a exécuté la commande dans son message réponse. 

En plus des macro, j'ai conservé la commande de DiceParser utilisée par les joueurs : 
! nb_dés d valeur_dés + bonus/malus
Par ex : !1d20-5

Calliope gère donc maintenant, en plus de ses autres fonctions :
  - les lancés de dés
  - les macro personnalisées pour les joueurs et joueuses de mon serveur.
  
Il n'y a plus qu'un bot sur mon serveur Discord pour éviter les conflits de commandes : Calliope. 
Elle est loin d'être aussi élaborée que DiceParser mais elle correspond pile aux besoin de mes groupes de JDR et je peux la personnaliser à l'envie.

