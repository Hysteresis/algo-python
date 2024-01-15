# Vous réutiliserez le code de l’exercice 3. Le but de votre programme est de créer une
# petite calculette :
#
# - L’utilisateur entrera successivement deux nombres, on vérifiera seulement
# qu’il ne laisse pas le champ vide
# - On lui demandera ensuite quel type de calcul il souhaite (faire
#         (addition, soustraction, division, multiplication))
# - On effectuera le calcul et on renverra la valeur à l’utilisateur
# - On demandera à l’utilisateur s’il souhaite faire un nouveau calcul ou quitter
# le programme

def calculate(val1, val2, op):
    if op == "+":
        result = float(val1) + float(val2)
        print(f"{num1} {operator}  {num2} = {result} ")
    if op == "-":
        result = float(val1) - float(val2)
        print(f"{num1} {operator}  {num2} = {result} ")
    if op == "*":
        result = float(val1) * float(val2)
        print(f"{num1} {operator}  {num2} = {result} ")
    if op == "/":
        result = float(val1) / float(val2)
        print(f"{num1} {operator}  {num2} = {result} ")



is_continue = True

print("Calculatrice")

while is_continue:
    num1 = ""
    num2 = ""
    operator = ""

    while num1 == "":
        num1 = input("Choississez nombre 1 : ")
        print(num1)

    while num2 == "":
        num2 = input("Choississez nombre 2 : ")

    while operator == "":
        operator = input("Choississez votre operateur (+  /  *  - ) : ")


    calculate(num1, num2, operator)


    continued = input("Voulez vous continuer : O / N : ")

    if continued == "o":
        is_continue = True
        print(is_continue)
    else:
        is_continue = False
        print(is_continue)



