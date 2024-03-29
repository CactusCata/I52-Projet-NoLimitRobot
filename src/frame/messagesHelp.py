""" Ce fichier python a pour objectif de stocker les messages d'aides pour chaque
fenêtre, afin de ne pas salir les autres fichiers."""

HELP_FMAIN = "Vous êtes les bienvenus dans notre jeu du nom de\n\n       NoLimitRobots\n\
\nCe jeu est une simulation de bataille de robots. Ceux-ci vont exécuter une série \
d'instructions, préalablement programmé par les joueurs, et se battront entre-eux \
pendant que vous observerez la partie. Oui-oui, vous n'aurez rien à \
faire si ce n'est prendre vos pop-corns et profiter du carnage (u.u)"

HELP_FSETTINGS = "Les options vous permettent de personnaliser votre expérience de \
jeu. Vous pourrez ainsi créer de nouvelles cartes, de nouveaux robots et changer \
certains aspects du jeu."

HELP_FCONFIGMAP = "Ici, vous pouvez créer de nouvelles cartes, ainsi que les éditer \
et les supprimer. Très utile si vous voulez tester vos tactiques avec des terrains \
plus uniques les uns que les autres."

HELP_FCREATEMAP = "Pour créer une nouvelle carte, on vous demande de rentrer un nom. \
Celui-ci doit être unique, donc il ne doit pas être identique avec un autre nom de carte. \
Une fois votre nom validé, vous serez renvoyés dans l'édition de la carte afin de la \
remplir."

HELP_FEDITMAP = "Vous voici dans le menu d'édition de la carte. Vous devez d'abord choisir \
une des cartes que vous avez créer, afin de la remplir ou de la modifier. Ainsi vous sont \
présentez plusieurs possibilités. Vous pouvez très bien vous contenter de créer la carte aléatoirement \
et la sauvegarder, mais vous avez aussi la possibilité de la créer vous même de rien ou bien d'un modèle \
générer par l'algorithme ou par un autre joueur.\nVous pouvez donc placer des rochers ou de l'air, mais \
attention, il ne faut pas avoir plus de 20% de rochers sur la carte, soit 120 rochers, sinon il vous sera \
impossible de sauvegarder vos modifications !"

HELP_FDELETEMAP = "Choisissez le nom de la carte que vous voulez supprimer puis confirmez votre choix"

HELP_FCONFIGROBOT = "Ici, vous pouvez créer de nouveaux robots, ainsi que les éditer \
et les supprimer. Très utile si vous voulez tester vos tactiques avec des robots \
plus uniques les uns que les autres."

HELP_FCREATEROBOT = "Nommez votre robot avec un nom différents de ceux déjà créé (vous pouvez rajouter un \
logo et une description si l'envie vous vient) puis sauvegarder celui-ci en cliquant sur 'Editer Robot' \
. Si vous quittez NoLimitRobots après avoir créer le robot, alors votre robot aura des instructions \
prédéfinies."

HELP_FEDITROBOT = "Vous pouvez modifier la description ou l'ajouter si celle-ci était vierge, puis vous \
pouvez modifier/ajouter des instructions autorisées afin de créer votre machine de guerre. Si vous voulez en \
savoir plus sur les fonctionnalités de chaque instruction, cliquez sur le menu déroulant à droite afin d'en \
apprendre plus sur ces dites instructions."

HELP_FDELETEROBOT = "Choisissez le nom de lu robot que vous voulez supprimer puis confirmez votre choix"

HELP_FDELETEPARTY = "/!\ WORK IN PROGRESS"

HELP_FPLAY = "Lancez une nouvelle partie, ou bien chargez une nouvelle partie (:I)"

HELP_FLOADPARTY = "/!\ WORK IN PROGRESS"

HELP_FPPLAYERCONFIG = "Dans ce menu vous devez choisir les robots pour chaque joueur. Ainsi vous \
devez choisir un des robots disponibles, puis confirmer celui-ci pour l'assigner à un joueur. \
Vous ne pouvez cliquer sur suivant uniquement si le nombre de joueur jouant (joueur possédant un robot) \
est compris entre 2 et 6."

HELP_FPPARTYCONFIG = "Sur ce menu vous pouvez modifier quelques options de la partie. Cela vous permet \
ainsi de diversifier votre expérience de jeu.\n\n\n\nVous pouvez donc modifier l'énergie des robots \
, énergie des robots étant leur points de vie ainsi que leur points d'actions pour effectuer leurs \
instructions, et modifier la distance de détection des robots.\n\nUn robot peut utiliser \
une instruction de test et pour cela utilisera cette dite distance de détection pour faire des choix \
d'instructions"

HELP_FPMAPCONFIG = "Choisissez la carte dans lequel vous souhaitez faire votre partie, puis passez \
à la suite. Vous aurez un visuel à droite de votre écran afin de voir à quoi ressemble la carte selectionnée.\n \
Sur ce visuel vous apercevrez un grand point d'interrogation si vous avez choisis le \"spread robots\"\
(positionnement aléatoire des robots), ou plusieurs points d'interrogations si vous avez choisis \"equidistance\"\
(positionnement des robots à une distance égale entre eux, donc sur les points d'interrogations)"

HELP_FPPARTY = "Vous voici enfin en partie ! Sur votre écran s'affiche un ensemble d'informations. Tout \
d'abord, vous avez la carte du jeu, avec vos robots se combattant dessus. Vous avez aussi à gauche de la carte \
vos robots en jeu avec leur niveau d'énergie. Bien-sûr si celui-ci est vide, cela voudra dire que votre robot \
sera déchargé. Enfin, sur la droite de la carte, vous rencontrerez un modificateur de vitesse de jeu, vous laissant \
le choix de changer la vitesse du jeu à tout moment. Si la molette de la barre de moletage est mise tout en haut, \
alors votre jeu sera mis en pause."
