# Comparer les deux tableaux et afficher l'élément identique entre les deux
# (utilisation de 2 boucles imbriquées)
i = 0
j = 0

foodOne = ['Noodle', 'Pasta', 'Ice-cream']
foodTwo = ['Fries', 'Ice-cream', 'Pizza']


for fone in range(len(foodOne)):
    for ftwo in range(len(foodTwo)):

        if foodOne[fone] == foodTwo[ftwo]:
            print(foodTwo[ftwo])

