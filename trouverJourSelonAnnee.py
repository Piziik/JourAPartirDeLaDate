##Programme qui trouve le jour selon une date donnée

#Définition des variables##
jour = int(input("Jour [JJ] : "))
mois = input("Mois [MM] : ")
annee = input("Année [AAAA] : ")
nombreMois = {"01": 0, "02": 3, "03": 3, "04": 6, "05": 1, "06": 4, "07": 6, "08": 2, "09": 5, "10": 0, "11": 3, "12": 5}
anneeDico = {"16": 6, "17": 4, "18": 2, "19": 0, "20": 6, "21": 4}
jourRecherche = {0: "Dimanche", 1: "Lundi", 2: "Mardi", 3: "Mercredi", 4: "Jeudi", 5: "Vendredi", 6: "Samedi"}
anneeBissextile = False
dateListe = [annee, mois, jour]

##Définit une année bissextile
if(int(annee)%4 == 0):
    if(int(annee)%100 == 0):
        if(int(annee)%400 == 0):
            anneeBissextile = True
    else:
        anneBissextile = True


finAnnee = int(dateListe[0][2:])##On garde les 2 derniers chiffres de l'année
jourSemaine = finAnnee + finAnnee//4##On ajoute 1/4 de ce nombre en ignorant le reste
jourSemaine = jourSemaine + jour ##On ajoute la journée du mois
jourSemaine = jourSemaine + nombreMois[mois] ##Selon le mois on ajoute

if anneeBissextile:
    if mois == "01" or mois == "02": ##Si année bissextile et le mois est janvier ou fevrier 
        jourSemaine+=-1 ##On enlève 1
    
debutAnnee = dateListe[0][0:2]##Selon le siècle on ajoute
jourSemaine = jourSemaine + anneeDico[debutAnnee]

reste = jourSemaine % 7 ##On garde le reste de la division par 7

print("Le jour de la date ", jour, "/", mois, "/", annee, "est un ", jourRecherche[reste])
