# Créer un algorithme effectuant la multiplication de 2 chiffres en utilisant uniquement des additions.
# Exemple: 2*3 = 3+3 = 6

i = 0
num1 = 4
num2 = 3
result = 0

for i in range(num1):
    if i < num1-1:
        print(num2, end=' + ')
        result += num2

    if i >= num1-1:
        result += num2
        print(num2, "= ", result)



