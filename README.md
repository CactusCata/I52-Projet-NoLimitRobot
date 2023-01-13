+====================================================================+

|| 												    ||

|| 					  NoLimitRobots 					    ||

|| 												    ||

+====================================================================+


x------------------------------------------------------------------------------------------------------------------------x

| (/o_o)/				  1 Introduction				    \(o_o\)  |

x------------------------------------------------------------------------------------------------------------------------x


	Bienvenue dans le README de notre jeu et merci de votre temps et de votre
 confiance que vous nous apportez en jouant à notre jeu. Avant toute chose, nous tenons à
 préciser que notre jeu n’est pas à son état final mais est actuellement en beta. Vous aurez
 donc accès au jeu en accès anticipé donc tout contenu présent dans cette version est sujet 
à de possibles changements et ajouts.

Ce jeu devrait marcher sous tout type de système d’exploitation, et il vous faudra le lancer 
via le fichier “main.py” présent dans le répertoire “src” du répertoire du jeu. Il vous faut donc
 sur votre machine un IDE ou bien un interprète python tel que python3 afin de pouvoir 
lancer le jeu. Si vous le lancez via un IDE, il vous faudra ouvrir votre IDE, charger le fichier
 main.py puis appuyer sur le bouton de la forme d’un triangle pointant vers la droite pour 
démarrer le jeu. Si vous le faites depuis un interprète installé sur votre machine, vous devrez
 lancer un terminal de commande et effectuer la commande de lancement du jeu. Par 
exemple, sur un système d’exploitation sous Linux, il vous faudra taper la commande 
“python3 main.py”, en vous trouvant bien sûr dans le même répertoire courant depuis votre 
terminal.



x------------------------------------------------------------------------------------------------------------------------x

| (/o_o)/				2 Droit à la propriété				    \(o_o\)  |

x------------------------------------------------------------------------------------------------------------------------x


	Toutes les entités graphiques en dehors de Tkinter, sont des propriétés intellectuelles
 en copyright libre ou créées par nous-même(Ne concerne que les entités présentes lors du 
téléchargement de l’application).


x------------------------------------------------------------------------------------------------------------------------x

| (/o_o)/				3 Rapport de bugs				    \(o_o\)  |

x------------------------------------------------------------------------------------------------------------------------x


	A l’heure actuelle, le nombre de bugs rapporté est très faible mais pas inexistant. Le 
seul “bug” que nous avons constaté est un bug lié à la configuration du pc. Si votre machine 
n’est pas très performante, il est possible qu’elle n’apprécie pas trop le changement brutal 
de vitesse de jeu durant la partie, causant ainsi un freeze de quelques secondes sur 
l’interface graphique.



///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	Cette partie maintenant ne concerne plus le README tel qu’il peut être dans le 
commerce mais concerne plutôt l’évaluation du projet. En effet, cette partie est plus

technique et aide à expliciter les choix de codes.


	Commençons par la structure de notre code. Nous sommes partis de la 
programmation modulaire, qui est absolument obligatoire à nos yeux pour un travail 
d’équipe. Pour synchroniser nos travaux, nous avons utilisé l’outil git et le site Github ce qui 
simplifie beaucoup la méthode de travail et nous évite beaucoup de temps perdu à éviter 
des conflits ou autres.
Nous avons fait le choix de créer de nombreux fichiers .py afin de simplifier les codes, nous 
permettant ainsi de voir tout notre code de manière bien net et précise, et nous permettant 
surtout d’avoir un grand confort lors de la programmation. On a donc un arbre ressemblant à 
ceci (grâce à la commande tree):

.
├── algopng.png
├── config
│   ├── maps
│   │   ├── new.dat
│   │   └── test.dat
│   ├── param.dat
│   └── robots
│   	├── truc
│   	│   ├── icon.png
│   	│   └── instructions.rbt
│   	├── tt
│   	│   ├── icon.png
│   	│   └── instructions.rbt
│   	└── wall-e
│       	├── icon.png
│       	└── instructions.rbt
├── launch.sh
├── LICENSE
├── pathfinding.txt
├── README.md
├── res
│   └── img
│   	├── icon.png
│   	├── map
│   	│   ├── air.png
│   	│   ├── ip.png
│   	│   ├── mine.png
│   	│   └── rock.png
│   	└── robot
│       	├── default_robot.png
│       	├── Hellbot.png
│       	├── Insomniabot.png
│       	└── Ketbot.png
├── src
│   ├── frame
│   │   ├── frames
│   │   │   ├── fMain.py
│   │   │   ├── party
│   │   │   │   ├── fLoadParty.py
│   │   │   │   ├── fPEndParty.py
│   │   │   │   ├── fPlay.py
│   │   │   │   ├── fPMapConfig.py
│   │   │   │   ├── fPPartyConfig.py
│   │   │   │   ├── fPParty.py
│   │   │   │   └── fPPlayerConfig.py
│   │   │   └── settings
│   │   │   	├── fSettings.py
│   │   │   	├── map
│   │   │   	│   ├── fConfigMap.py
│   │   │   	│   ├── fCreateMap.py
│   │   │   	│   ├── fDeleteMap.py
│   │   │   	│   └── fEditMap.py
│   │   │   	├── party
│   │   │   	│   └── fDeleteParty.py
│   │   │   	└── robot
│   │   │       	├── fConfigRobot.py
│   │   │       	├── fCreateRobot.py
│   │   │       	├── fDeleteRobot.py
│   │   │       	└── fEditRobot.py
│   │   ├── iFrame.py
│   │   ├── messagesHelp.py
│   │   └── rootManager.py
│   ├── game
│   │   └── game.py
│   ├── image
│   │   └── imageManager.py
│   ├── instruction
│   │   ├── instructionAnalyser.py
│   │   ├── instructionList
│   │   │   ├── al.py
│   │   │   ├── dd.py
│   │   │   ├── ft.py
│   │   │   ├── iInstruction.py
│   │   │   ├── inn.py
│   │   │   ├── mi.py
│   │   │   ├── ps.py
│   │   │   ├── th.py
│   │   │   ├── tt.py
│   │   │   └── tv.py
│   │   ├── instructionSyntaxException.py
│   │   ├── instructLexicalAnalyser.py
│   │   └── instructSyntaxAnalyser.py
│   ├── instructTest.py
│   ├── main.py
│   ├── main_test.py
│   ├── map
│   │   ├── mapDrawer.py
│   │   ├── mapManager.py
│   │   ├── map.py
│   │   └── mine.py
│   ├── param
│   │   ├── paramManager.py
│   │   └── param.py
│   ├── player
│   │   ├── playerManager.py
│   │   └── player.py
│   ├── robot
│   │   ├── robotChooser.py
│   │   ├── robotFile.py
│   │   ├── robotManager.py
│   │   └── robotParty.py
│   └── utils
│   	├── fileUtils.py
│   	├── imageUtils.py
│   	├── instructionUtils.py
│   	├── mapUtils.py
│   	├── mathsUtils.py
│   	├── otherUtils.py
│   	├── robotUtils.py
│   	└── tkinter
│       	├── tkPerformer.py
│       	└── tkUtils.py
└── todo.txt

Chose importante à ajouter, nous étions partis sur un projet très ambitieux, mais au vu des 
consignes demandées ainsi que du temps que cela prenait, nous avons réduit les tâches à 
faire. Cependant, nous avons conscience que nous avons ajouté beaucoup de notions non 
demandées telles que la création de robot/carte dans le jeu. Nous voulions à tout prix le 
faire, afin d’avoir un rendu qui faisait vraiment jeu ergonomique et proposant beaucoup de 
liberté. C’était une de nos plus grandes priorités de pouvoir faire en sorte que n’importe 
quelle personne puisse jouer à ce jeu sans être déboussolée et sans n’avoir aucune 
compétence en informatique si ce n’est cliquer sur un png dans un répertoire.
Autre chose, il y a des choses que l’on voulait faire qui sont actuellement proposées à 
l’utilisateur mais qui ne sont pas codées, tel que la sauvegarde de partie et le chargement 
de partie.


	Parlons de la structure elle-même maintenant. Celle-ci a été divisée de la manière 
qui nous semblait la plus cohérente. Par exemple, on a regroupé dans le répertoire ‘frame’ 
les fenêtres du jeu, on a regroupé les messages d’aide dans un fichier appelée 
‘messagesHelp.py’ ou bien encore nous avons regroupé les données telles que les cartes et 
les robots dans un répertoire ‘config’.



	Parlons de la technique, concernant ce que nous appelons les ‘frames’, i.e les 
fenêtres affichées dans notre fenêtre mère, nous avons procédé par un paradigme de POO. 
Ainsi, nous avons le fichier ‘Iframe.py’ qui est la classe mère de toutes les autres frames. 
Celle-ci est une classe manipulant la création de widgets et autres objets de Tkinter mais de 
manière à simplifier et optimiser le développement. Par exemple, lorsqu’on utilise une 
méthode de la classe Iframe dans un fichier avec pour contenu une classe fille de Iframe, on 
va stocker dans une liste le widget que l’on aura créé avec la méthode utilisée.
On utilise cette liste ayant comme éléments tous les widgets, canvas, car la stratégie 
abordée est de supprimer tous les éléments graphiques sur la fenêtre lorsqu’on passe d’une 
fenêtre à l’autre. Procédé : Suppression des objets de la fenêtre actuelle, stockés dans la 
liste -> Création et affichage des objets de la nouvelle fenêtre.

Pour les objets graphiques, nous avons fait en sorte de les afficher de manière à ce que 
ceux-ci puissent s’adapter à la taille de la fenêtre. On a donc utilisé pack de tkinter, 
puisqu’on a fait le choix de laisser à l’utilisateur la possibilité de changer la taille de la 
fenêtre. Pour cela, celui-ci a le choix entre laisser la fenêtre telle qu’elle est initialement en 
fenêtrée, ou bien de la mettre en plein écran. Cette option ainsi que l’option d’activation de 
l’aide sont modifiables dans le menu des options du jeu. Ces choix d’utilisateurs sont 
stockés dans des fichiers grâce au module JSON de python (qu’il vous faudra donc sur votre 
machine).
Durant l’application, des images en format png seront nécessaires, et pour éviter toute 
latence redondante et coûteuse, on a décidé de précharger les images lors du lancement du 
jeu. Ainsi, lorsqu’elles seront utilisées notamment lors de la partie, on aura déjà en mémoire 
les photos.


Par rapport aux robots et à la carte, nous avons aussi opté pour de la POO car cela 
est très pratique et confortable.
En fait, en regardant le code, vous remarquerez que nous n’avons fait quasiment que de la 
POO; on a jugé que c’était une bonne méthode de travail pour ce projet.
Pour les robots, les instructions de poursuite et de fuite fonctionnent par un système de 
pathfinding. Celui-ci a été inspiré de celui présent sur cette vidéo youtube : 
https://www.youtube.com/watch?v=-L-WgKMFuhEY
On a donc utilisé la distance euclydienne, la distance tchebychev et un mélange des deux 
qu’on a appelé la distance chareyre.

Nous avons aussi fait de la gestion d’erreur, parfois elle est exprimée 
explicitement(ex : Si un robot est sauvegardé mais n’a pas de nom, un message s’affiche 
sur l’écran pour dire à l’utilisateur qu’il manque un nom non utilisé), tandis que parfois elle 
est implicite (ex : Pour le choix des robots à mettre en jeu, si le nombre de joueur est 
inférieur à 2, alors l’utilisateur ne peut cliquer sur Suivant), et dans la plus grande partie de 
notre code, on a programmé de manière à empêcher les erreurs possibles.
On a aussi fait un analyseur lexical et syntaxique dans l’éditeur de robot afin d’éviter tout 
problème dit mortel pour le jeu. L’utilisateur ne pourra donc qu’écrire les instructions 
autorisées et au bon endroit.


	Pour l’aspect graphique, certaines choses liées à la structuration du projet ont été 
précédemment dites, ce que l’on va ajouter et que certaines animations ne sont pas 
présentées visuellement mais fonctionnent bien; on pensera en l'occurrence à la fonction IN 
qui ne rend pas visuellement invisible le robot mais fonctionnellement il l’est, ainsi qu’aux tirs 
des robots que l’on ne verra pas.


PS: On a juste changé un concept : pour la commande AL, on a fait en sorte que le robot se 
déplace dans tous les cas dans une distance possible, et non pas qu’il reste bloqué si sa 
distance choisie aléatoirement n’est pas libre. On voulait peaufiner un peu la jouabilité ainsi.
Autre chose à ajouter, on a utilisé un outil du nom de Gource permettant de voir l’évolution 
du projet; voici le lien (attention c’est très addictif) : https://youtu.be/jVNXMSyYhCY