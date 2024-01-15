# Créer un algorithme demandant à l'utilisateur un chiffre'
# ' et lui afficher la table de multiplication correspondante. (jusqu')à 10)

get_number = input("Saisir un chiffre :")

print(f"Table de multiplicaiton de {get_number}")

for i in range(11):
    result = i * (int(get_number))
    print(f"{i} x {get_number} = {result} ")
