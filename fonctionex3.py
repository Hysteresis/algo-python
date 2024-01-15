# Votre programme consistera à afficher des textes selon le choix de l’utilisateur.
# Vous demanderez à l’utilisateur de choisir un nombre en 1 et 4. Pour chaque choix,
# vous afficherez une alert() avec le choix sélectionné.

print("quel jour sommes nous ?")
jour = input()


print(f"Choix {jour} :")

match jour:
    case "1":
        print("Lundi")
    case "2":
        print("Mardi")
    case "3":
        print("Mercredi")
    case "4":
        print("Jeudi")
    case "5":
        print("Vendredi")


