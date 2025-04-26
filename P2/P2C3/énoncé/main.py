# Vous devez créer un programme qui calcule le salaire horaire d'un employé, en fonction de son salaire mensuel et de son nombre 
# d'heures travaillées par semaine

# Calculez le salaire mensuel d'un employé à partir de son salaire annuel


def salaire_mensuel(salaire_annuel):
    salaire_mensuel = float(salaire_annuel) / 12
    return salaire_mensuel

# Calculez le salaire hebdomadaire d'un employé à partir de son salaire mensuel
def salaire_hebdomadaire(salaire_mensuel):
    salaire_hebdomadaire = float(salaire_mensuel) / 4
    return salaire_hebdomadaire

# Calculez le salaire horaire d'un employé à partir de son salaire hebdomadaire
def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    taux_horaire = float(salaire_hebdomadaire) / float(heures_travaillees)
    return round(taux_horaire, 2)

# Demander le salaire annuel
salaire_annuel = input("Entrez le salaire annuel de l'employé : ")

# Demander les heures travaillées par semaine
heures_travaillees = input("Entrez votre volume d'heure de travaille par semaine : ")

# Calcul du salaire horaire
mon_salaire_mensuel = salaire_mensuel(salaire_annuel)
mon_salaire_hebdomadaire = salaire_hebdomadaire(mon_salaire_mensuel)
mon_salaire_horaire = salaire_horaire(mon_salaire_hebdomadaire, heures_travaillees)

# Affichage du salaire horaire
print(f"Votre salaire horaire est de : {mon_salaire_horaire} $ ")
