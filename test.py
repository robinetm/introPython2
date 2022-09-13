
# Crée par Mathis Robinet
# Crée en 2020
# Jeu RPG

# didactiticiel
from random import randint

# présentation

print("Bonjour, je m'appelle Bob et je vais t'aider pendant ton séjour dans le didacticiel .")
nom_joueur = str(input("comment te nommes-tu ? : "))
print(
    "Bonjour %s heureux de te connaitre .\n==============================================================================" % (
        nom_joueur))
# choix
print(
    "Commençon, commence par choisir ta classe \n 1-mage \n Le mage a 250 de vie et 50 d'attaque max \n 2-guerrier \n Le guerrier a 500 de vie et 30 d'attaque max  ")
print(
    " 3- assassin. \n l'assassin a 200 de vie et 70 d'attaque max .\n ===================================================================")

choix_classe = int(input(" écris le numéro de la classe que tu veux choisir. \n "))
if choix_classe == 1:
    print(
        "bon choix . le mage est un tres bon personnage. ses Stats son équilibrer.  \n==============================================================================")
    attaque = 50
    vie = 250
    vieMax = 250
if choix_classe == 2:
    print(
        "bon choix . le guerrier est un tres bon personnage. Il a beucoup de vie mais il fait moins mal. \n==============================================================================")
    attaque = 36
    vie = 500
    vieMax = 500
if choix_classe == 3:
    print(
        "bon choix . l'assassin est un tres bon personnage. Il fait tres mal mais il a moins de vie \n==============================================================================")
    attaque = 70
    vie = 200
    vieMax = 200
# Introduction au combat
degat25 = 25 * attaque / 100
degat50 = 50 * attaque / 100
print(
    "Pour commencer tu va te battre contre un goblin. \n Tu as trois choix d'attaque,  \n attaquer avec tes poing qui a 100%% de chance de réussir mais il  fait  %d dégat " % (
        degat25))
print(
    " ,attaquer avec ton arme qui a 50%% de chance de réussir mais il fait %d dégat, \n attaquer avec tes pouvoir qui a 20%% de chance de réussir mais il fait %d dégat." % (
    degat50, attaque))
print(" ==============================================================================")

#################################
##combat goblin
################################
vie_goblin = 60
while vie_goblin > 0 and vie > 0:
    attaque_goblin = str(input(
        "Le goblin a %d de vie et 20 d'attaque qu'allez-vous faire, coup de poing, coup d'épée, pouvoir." % (
            vie_goblin)))
    vie_goblinCoupPoing = vie_goblin - degat25

    if attaque_goblin == "coup de poing":
        pourc_reussitePoing = randint(1, 10)
        if pourc_reussitePoing < 10:
            degat = degat25
        else:
            degat = 0

    elif attaque_goblin == "pouvoir":
        pourc_reussitePouvoir = randint(1, 3)
        if pourc_reussitePouvoir == 3:
            degat = attaque
        else:
            degat = 0

    elif attaque_goblin == "coup d'épée":
        pourc_reussiteÉpée = randint(1, 2)
        if pourc_reussiteÉpée == 2:
            degat = degat50
        else:
            degat = 0

    if degat > 0:
        vie_goblin = vie_goblin - degat
        print("vous avez fait %d dégat, le goblin a %d de vie  " % (degat, vie_goblin))
    else:
        vie -= 20
        print("Votre attaque a échoué, le goblin vous a infligé 20 de dégat, Vous avez maintenant %d de vie." % (vie))

if vie_goblin < 1:
    vie = vieMax
    vie += 20
    attaque += 10
    print("comme tu a battue ton premier enemie tu a %d de vie et %d d'attaque. " % (vie, attaque))

# =========================================================================================================================================================================================================================================


# intruduction de l'histoire
print("==============================================================================")
print(
    "C'est ici que s'acheve mon aventure a tes cotés %s. Tu devras poursuivre seul a partir de maintenant. Maintenant que tu as terminé le didacticiel tu es près pour t'aventurer dans les terres longtaine de sepulcretum.Ton but est d'aller secourir mon frère emprisoner par le dragon Zorox, je te souehtte bonne chance. Petit conseil, fait attention a ou tu mets tes pied." % (
        nom_joueur))

#################################
##combat squelette
################################
if vie > 0:
    print("==============================================================================")
    print(
        "Vous commencer a marcher dans cette univers et vous marchez accidentellement sur un os. Cette os était le bras d'un squelette et il n'a pas plus que vous le réveillez pendant son someille.")
    print(
        "Il commence a vous pourchassez avec une jambe de son compagnon dans sa main. Vous avez plus le choix, vous etes a boue de souffle et vous ne pouvez plus vous enfuir. Vous devez combattre !")

vie_squelette = 100
while vie_squelette > 0 and vie > 0:
    attaque_squelette = str(input(
        "Le squelette a %d de vie et 40 d'attaque qu'allez-vous faire, coup de poing, coup d'épée, pouvoir." % (
            vie_squelette)))
    vie_squeletteCoupPoing = vie_squelette - degat25

    if attaque_squelette == "coup de poing":
        degat = degat25
        pourc_reussitePoing = randint(1, 10)
        if pourc_reussitePoing < 10:
            degat = degat25
        else:
            degat = 0

    elif attaque_squelette == "pouvoir":
        degat = attaque
        pourc_reussitePouvoir = randint(1, 3)
        if pourc_reussitePouvoir == 3:
            degat = attaque
        else:
            degat = 0

    elif attaque_squelette == "coup d'épée":
        degat = degat50
        pourc_reussiteÉpée = randint(1, 2)
        if pourc_reussiteÉpée == 2:
            degat = degat50
        else:
            degat = 0

    if degat > 0:
        vie_squelette = vie_squelette - degat
        print("vous avez fait %d dégat, le squelette a %d de vie  " % (degat, vie_squelette))
    else:
        vie -= 40
        print(
            "Votre attaque a échoué, le squelette vous a infligé 40 de dégat, Vous avez maintenant %d de vie." % (vie))

if vie_squelette < 1:
    vie = vieMax
    vie += 20
    attaque += 10
    print(
        "Bien jouer vous avez tué le squelette mais en même temps le loup a senti les os et a été attiré. Vous avez %d de vie et %d d'attaque " % (
        vie, attaque))

#################################
##combat loup
################################
if vie > 0:
    print("==============================================================================")
    print(
        "Le loup commence a tourne autour de vous étant faché que car vous venez juste de lui voler son gouter. Sans perdre de temps il sauta sur vous !")
vie_loup = 180
while vie_loup > 0 and vie > 0:
    attaque_loup = str(input(
        "Le loup a %d de vie et 50 d'attaque qu'allez-vous faire, coup de poing, coup d'épée, pouvoir." % (vie_loup)))
    vie_loupCoupPoing = vie_loup - degat25

    if attaque_loup == "coup de poing":
        degat = degat25
        pourc_reussitePoing = randint(1, 10)
        if pourc_reussitePoing < 10:
            degat = degat25
        else:
            degat = 0

    elif attaque_loup == "pouvoir":
        degat = attaque
        pourc_reussitePouvoir = randint(1, 3)
        if pourc_reussitePouvoir == 3:
            degat = attaque
        else:
            degat = 0

    elif attaque_loup == "coup d'épée":
        degat = degat50
        pourc_reussiteÉpée = randint(1, 2)
        if pourc_reussiteÉpée == 2:
            degat = degat50
        else:
            degat = 0

    if degat > 0:
        vie_loup = vie_loup - degat
        print("vous avez fait %d dégat, le loup a %d de vie  " % (degat, vie_loup))
    else:
        vie -= 50
        print("Votre attaque a échoué, le loup vous a infligé 40 de dégat, Vous avez maintenant %d de vie." % (vie))

if vie_loup < 1:
    vie = vieMax
    vie += 15
    attaque += 10

    griffe_loup = randint(1, 3)
    fourrure_loup = randint(1, 3)

    print(
        "Le loup s'écroule sur le tat dos tout comme vous a cause de vos 2 combat fait d'affiler. Vous perder 5 de vie.Vous avez %d de vie et %d d'attaque " % (
        vie, attaque))

    if griffe_loup == 3:
        attaque += 20
        print(
            "La chance vous sourie le loup a fait tomber sa griffe avant de disparaitre dans un éclat de fumée. Vous avez maintenant %d d'attaque." % (
                attaque))
    if fourrure_loup == 3:
        vie += 40
        print(
            "La chance vous sourie le loup a fait tomber sa fourrure avant de disparaitre dans un éclat de fumée. Vous avez maintenant %d de vie." % (
                vie))
    if griffe_loup and fourrure_loup == 3:
        vie += 90
        attaque += 45
        print(
            "Le loup vous remercie de l'avoir tué sur un tat d'os c'était son rêve d'être sur un tat d'os toute sa vie. Il vous donne un compagnon loup qui vous suivra partout.Vous avez maintenant %d d'attaque et %d de vie." % (
            attaque, vie))

##Village
print("==============================================================================")

if vie > 0:
    vie += 30
    attaque += 20
    print(
        "vous marchez des minutes et des heure sans trouver un endroit ou se reposer. Soudain, vous voyez un village qui semble habiter avec des villagois aceuillant. Vous les demandez ou trouvez le dragon zorox. Surpris de votre question ils vous demandèrent de répéter. les villagois dit que zorox est au nord ouest d'ici. Ils vous donnère de l'équipement pour vous aider a le combattre. Vous remerciez les villagois de leur acceuille chaleureux et partie ver le nord ouest. Vous avez maintenant %d d'attaque et %d de vie." % (
        attaque, vie))

#################################
##combat ogre
################################
if vie > 0:
    print("==============================================================================")
    print(
        "Vous marcher vers la direction dit par les villagois et un ogre vous bloqua le passage. Puis il sauta sur vous!")
vie_ogre = 220
while vie_ogre > 0 and vie > 0:
    attaque_ogre = str(input(
        "Le ogre a %d de vie et 50 d'attaque qu'allez-vous faire, coup de poing, coup d'épée, pouvoir." % (vie_ogre)))
    vie_ogreCoupPoing = vie_ogre - degat25

    if attaque_ogre == "coup de poing":
        degat = degat25
        pourc_reussitePoing = randint(1, 10)
        if pourc_reussitePoing < 10:
            degat = degat25
        else:
            degat = 0

    elif attaque_ogre == "pouvoir":
        degat = attaque
        pourc_reussitePouvoir = randint(1, 3)
        if pourc_reussitePouvoir == 2:
            degat = attaque
        else:
            degat = 0

    elif attaque_ogre == "coup d'épée":
        degat = degat50
        pourc_reussiteÉpée = randint(1, 2)
        if pourc_reussiteÉpée == 2:
            degat = degat50
        else:
            degat = 0

    if degat > 0:
        vie_ogre = vie_ogre - degat
        print("vous avez fait %d dégat, le ogre a %d de vie  " % (degat, vie_ogre))
    else:
        vie -= 50
        print("Votre attaque a échoué, le ogre vous a infligé 40 de dégat, Vous avez maintenant %d de vie." % (vie))

if vie_ogre < 1:
    vie = vieMax
    vie += 35
    attaque += 25

    massue_ogre = randint(1, 3)
    peau_ogre = randint(1, 3)

    print(
        "Tout le corp de se gros colosse tombat et fit un tremblement de terre qui retenti a des kilomètre.Vous avez %d de vie et %d d'attaque " % (
        vie, attaque))

    if massue_ogre == 3:
        attaque += 30
        print(
            "D'un gros coup vous l'achevé et son corp disparie par chance sa massue ne disparie pas avec lui . Vous avez maintenant %d d'attaque." % (
                attaque))
    if peau_ogre == 3:
        vie += 50
        print(
            "D'un gros coup vous l'achevé. Un dragon aparut et aspira tout l'ogre en lessant que ca peau. Une chance qu'il ne vous a pas vue, mais vous finirer surement par tomber nez a nez contre lui. Vous avez maintenant %d de vie." % (
                vie))

    if massue_ogre and peau_ogre == 3:
        vie += 100
        attaque += 50
        print(
            "le roi des ogre vous a vue et il vous donne un compagnon ogre qui vous suivra partout.Vous avez maintenant %d d'attaque et %d de vie." % (
            attaque, vie))

#################################
##combat Dragon
################################
if vie > 0:
    print("==============================================================================")
    print(
        "Vous avanca quelque kilomètre plus loing et tomna juste devant la grotte du dragon. Vous y entrez et le vis assis sur les os de tous c'est victime. vous tourna la tete et vis le frere de bob emprisonner. Vous vous empresez d'aller l'aider mais le dragon s'y opposa et commenca a cracher du feu. Il commenca a vous attaquer  !")
vie_Dragon = 250
while vie_Dragon > 0 and vie > 0:
    attaque_Dragon = str(input(
        "Le Dragon a %d de vie et 60 d'attaque qu'allez-vous faire, coup de poing, coup d'épée, pouvoir." % (
            vie_Dragon)))
    vie_DragonCoupPoing = vie_Dragon - degat25

    if attaque_Dragon == "coup de poing":
        degat = degat25
        pourc_reussitePoing = randint(1, 10)
        if pourc_reussitePoing < 10:
            degat = degat25
        else:
            degat = 0

    elif attaque_Dragon == "pouvoir":
        degat = attaque
        pourc_reussitePouvoir = randint(1, 3)
        if pourc_reussitePouvoir == 2:
            degat = attaque
        else:
            degat = 0

    elif attaque_Dragon == "coup d'épée":
        degat = degat50
        pourc_reussiteÉpée = randint(1, 2)
        if pourc_reussiteÉpée == 2:
            degat = degat50
        else:
            degat = 0

    if degat > 0:
        vie_Dragon = vie_Dragon - degat
        print("vous avez fait %d dégat, le Dragon a %d de vie  " % (degat, vie_Dragon))
    else:
        vie -= 60
        print("Votre attaque a échoué, le Dragon vous a infligé 40 de dégat, Vous avez maintenant %d de vie." % (vie))

    if vie_Dragon < 1:
        vie = vieMax
        vie += 100
        attaque += 25
        print(
            "L'imense monstre s'envola ayant peur de mourir mais vous le rattrapa et lui achevez le coup de grace .Vous couri vers le frere de bob et le libérez. Soudain vous sentit une étrange puissance maléfique et vous voyez bob et son frere transformer en démon et il dit.«HAHAHA JE T'AI EU MON POUVOIR NE POUVAIT PAS ÊTRE COMPLÉ SANS MON FRÈRE ET MAINTENANT QUE TU A TUÉ LE GARDIEN DU TEMPLE PLUS PERSONNE POURRA M'ARRÉTER».Vous avez %d de vie  et %d d'attaque" % (
            vie, attaque))

    dent_dragon = randint(1, 3)
    écaille_dragon = randint(1, 3)

    if dent_dragon == 3:
        attaque += 80
        print("Le dragon Laissas tombé une de ses dents. Vous avez maintenant %d d'attaque." % (attaque))
    elif écaille_dragon == 3:
        vie += 200
        print(
            "Avant de mourir et de disparaitre une écaille de dragon tombie du ciel.  Vous avez maintenant %d de vie." % (
                vie))

    elif dent_dragon and écaille_dragon == 3:
        vie += 900
        attaque += 500
        print(
            "Vous pouver fabriquer une compagnon dragon avec ses deux objet.Vous avez maintenant %d d'attaqie et %d de vie" % (
            attaque, vie))

#################################
##combat Bob
################################
if vie > 0:
    print("==============================================================================")
vie_Bob = 300
while vie_Bob > 0 and vie > 0:
    attaque_Bob = str(input(
        "Le Bob a %d de vie et 70 d'attaque qu'allez-vous faire, coup de poing, coup d'épée, pouvoir." % (vie_Bob)))
    vie_BobCoupPoing = vie_Bob - degat25

    if attaque_Bob == "coup de poing":
        degat = degat25
        pourc_reussitePoing = randint(1, 3)
        if pourc_reussitePoing == 2:
            degat = degat25
        else:
            degat = 0

    elif attaque_Bob == "pouvoir":
        degat = attaque
        pourc_reussitePouvoir = randint(1, 3)
        if pourc_reussitePouvoir == 2:
            degat = attaque
        else:
            degat = 0

    elif attaque_Bob == "coup d'épée":
        degat = degat50
        pourc_reussiteÉpée = randint(1, 3)
        if pourc_reussiteÉpée == 2:
            degat = degat50
        else:
            degat = 0

    if degat > 0:
        vie_Bob = vie_Bob - degat
        print("vous avez fait %d dégat, le Bob a %d de vie  " % (degat, vie_Bob))
    else:
        vie -= 70
        print("Votre attaque a échoué, le Bob vous a infligé 70 de dégat, Vous avez maintenant %d de vie." % (vie))

if vie_Bob < 1:
    vie = vieMax
    vie += 1000000
    attaque += 9999999

print("==============================================================================")
if vie < 1:
    for i in range(50):
        print(i * " " + "Vous avez perdue ")
else:
    for i in range(4):
        for j in range(50):
            print(j * " " + "Vous avez Gagné !! ")

