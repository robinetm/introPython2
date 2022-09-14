# Crée par Mathis Robinet
# Crée en 22/09/14
# TP1

chaine = input("ecris un mot ou des mots en verifiant qu'il n'y ai d'espace qu'entre les mots:") #question qui dit d'écrire un ou des mots pour les compter


def word_count():                           #fonction pour compter le nombre de mots
    espace = (" " in chaine)                #regarde si il y a des espace dans le code
    if espace == True:                      #si il y a un espace↓
        NbrEspace = (chaine.count(" "))     #compte le nombre d'espace
        NbrMots = NbrEspace + 1             #ajoute +1 au nombre d'espace pour trouver le nombre de mots
        print("il y a %d mots dans ce que vos avez écris." % (NbrMots))         #dit il y a combien de mots dans les mots choisis plus haut
        
word_count()      #lance la fonction
