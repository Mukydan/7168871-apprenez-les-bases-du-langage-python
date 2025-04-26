# Ecrivez notre code ici !
nombres = input('saississez une liste de nombres séparés par des virgules : ')
print(nombres)
# Utiliser la méthode split() pour transformer la variable nombres en une liste
# de nombres
liste = nombres.split(',')
print(liste)
# Transformer la liste en une liste d'entiers
liste_entiers = []
for i in range(len(liste)):
    liste_entiers.append(int(liste[i]))
print(liste_entiers)

# Calculer et afficher la somme des nombres de la liste
somme = 0
for i in range(len(liste_entiers)):
    somme += liste_entiers[i]
print(f"La somme des nombres de la liste est : {somme} ")

# Calculer et afficher la moyenne des nombres de la liste
moyenne = somme  / len(liste_entiers)
print(f"La moyenne des nombre de la liste est : {moyenne}")

# Calculer et afficher le nombre de nombres dans la liste qui sont supérieurs
# à la moyenne
compteur = 0
for i in range(len(liste_entiers)):
    if liste_entiers[i] > moyenne:
        compteur += 1
print(f"le nombre de nombres supérieurs à la moyenne est : {compteur}")
