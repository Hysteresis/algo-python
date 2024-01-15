# Votre programme consistera à demander à l’utilisateur de rentrer le nom de la marque des
# voitures qu’il a pu posséder. Entre chaque voiture, vous demanderez à l’utilisateur s’il veut
# rajouter une nouvelle voiture.
# Vous stockerez
# les valeurs dans un tableau et afficherez les valeurs de ce tableau à la fin du programme.

voitures = []
is_continue = True
while is_continue:
    def ajouter_voiture(voiture):
        voitures.append(voiture)

    car = input("Entrer le nom de votre voiture :")
    ajouter_voiture(car)

    response = input("Voulez-vous continuer ? O/F ")

    if response == "o":
        is_continue = True
        print(is_continue)
    else:
        is_continue = False
        print(is_continue)

for voiture in voitures:
    print(f"Nom : {voiture}  ")