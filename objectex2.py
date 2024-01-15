# Votre programme consistera à demander à l’utilisateur le nombre d’animaux
# qu'il a possédé d'un certain type (chat, chien, lapin ou autre).
# Vous demanderez ensuite autant de fois les noms des animaux.
# Vous stockerez les valeurs dans un tableau.
# // Si l'utilisateur veut donner le nom de ces chats, le résultat final sera:
# // ['Mimi', 'Minou', 'Levis', 'Tic', 'Tac']
# Vous afficherez ensuite à l’utilisateur les valeurs de l’objet.

i = 0
categories = ["chat", "chien", "lapin", "autre"]
noms = []
print("Categories :")

for categorie in categories:
    i += 1
    print(f" {i} - {categorie}")

choice = input("Choisissez la categorie : ")

is_continue = True
while is_continue:
    # if choice == "0":

    saisir = input("Saisir le nom : ")

    noms.append(saisir)



    response = input("Voulez-vous continuer ? O/F ")

    if response == "o":
        is_continue = True
        print(is_continue)
    else:
        is_continue = False
        print(is_continue)



print("------------------------------------")
print("Voici le nom de vos animaux : ")
print("------------------------------------")
for n in noms:
    print(n)