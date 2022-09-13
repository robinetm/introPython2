questionAN = int(input("en quelle année est tu née?"))
questionMN = str(input("en quelle mois es-tu né?"))
questionJN = int(input("tu es né le combien?"))
questionAA = int(input("et en quelle année nous somme?"))
questionMA = str(input(" quelle mois nous somme?"))
questionJA = int(input("nous somme le combien?"))

age: int = questionAA - questionAN

if questionMN == questionMA:
    if questionJN == questionJA:
        print("tu as %d" % (age))

else:
    print("tu as %d"% (age-1))

