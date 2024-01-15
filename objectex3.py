# Votre programme consistera à demander à l’utilisateur le nombre d’animaux
# qu'il a possédé d'un certain type (chat, chien, lapin ou autre).
# Vous demanderez ensuite autant de fois les noms des animaux.
# Vous stockerez les valeurs dans un tableau.
# // Si l'utilisateur veut donner le nom de ces chats, le résultat final sera:
# // ['Mimi', 'Minou', 'Levis', 'Tic', 'Tac']
# Vous afficherez ensuite à l’utilisateur les valeurs de l’objet.
# vous permettrez à l’utilisateur de modifier l’une des valeurs qu’il a remplies,
# puis vous lui réafficherez les nouvelles valeurs.

def afficher_noms(names):
    i = 0
    for n in names:
        i += 1
        print(f" {i} - {n}")

categories = ["chat", "chien", "lapin", "autre"]
animaux = {}
noms = []


# print(noms.keys())
# print(noms.values())

nb_animals = input("Combien d'animaux : ")

i = 0

# Lister les  catégories
for categorie in categories:
    i += 1
    print(f"{i} - {categorie} ")

# demander à l’utilisateur la catégorie
nb_categories = input("Quelle catégorie ? : ")

# Saisir tous les animaux
for i in range(int(nb_animals)):
    name = input(f"Nom du {categories[int(nb_categories) - 1]}: ")
    noms.append(name)
print("\n------------------------")
print(f"Les noms des {categories[int(nb_categories) - 1]}s sont : ")
print("--------------------------")


afficher_noms(noms)


print("Voulez vous modifier un nom ?")
modification_nom = int(input())

print("je veux modifier ", noms[modification_nom - 1])
new_nom = input("Quel est son nouveau nom")
noms[modification_nom - 1] = new_nom

afficher_noms(noms)

