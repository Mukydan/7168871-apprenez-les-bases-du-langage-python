# Ecrivez votre code ici
# Concevoir une calculatrice simple qui effectue les opérations suivantes :
# addition, soustraction, multiplication et division.

# Demander à l'utilisateur de fournir deux nombres nombre1 et nombre2
nombre1 = input("Entrez le premier nombre : ")
nombre2 = input("Entrez le deuxième nombre : ")
# Vérifier si les entrées sont des nombres
if nombre1.isnumeric() and nombre2.isnumeric():
    # Convertir les entrées en entiers
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)
else:
    # Si les entrées ne sont pas des nombres, afficher un message d'erreur
    # et quitter le programme
    raise SystemExit("Fin du programme, les deux nombres doivent être des entiers")

# Demander à l'utilisateur de choisir une opération parmi les suivantes :
# +, -, *, /
operation = input("Entrez l'opération (*, /, +, -) : ")
if operation == '+':
    resultat = nombre1 + nombre2
elif operation == '-':
    resultat = nombre1 -  nombre2
elif operation == '*':
    resultat = nombre1 * nombre2
elif operation == '/':
    # Vérifier si le deuxième nombre est différent de zéro avant de diviser
    # Si le deuxième nombre est zéro, afficher un message d'erreur
    # et quitter le programme
    # Si le deuxième nombre est différent de zéro, effectuer la division
    # et arrondir le résultat à deux décimales
    if nombre2 == 0:
        raise SystemExit('Erreur : Division par zéro')
    else:
        resultat = round(nombre1 /nombre2, 2)
else:
    raise SystemExit('Erreur : Opération non valide')
# Afficher le résultat de l'opération choisie
print(f"Le résultat de {nombre1} {operation} {nombre2} est : {resultat}")
