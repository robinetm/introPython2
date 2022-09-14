# Crée par Mathis Robinet
# Crée en 22/09/14
# TP1

chaine = input("ecris un mot ou des mots en verifiant qu'il n'y ai d'espace qu'entre les mots:")


def word_count():
    espace = (" " in chaine)
    if espace == True:
        NbrEspace = (chaine.count(" "))
        NbrMots = NbrEspace + 1
        print("il y a %d mots dans ce que vos avez écris." % (NbrMots))
        
word_count()
