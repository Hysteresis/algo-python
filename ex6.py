# Vérifier qu'une chaine de caractère est un palindrome ou non.
# Exemple: le mot kayak ou bien 1661

mot = "166"
i = 0
is_palindrome = True

for i in range(len(mot)):
    if mot[i] == mot[len(mot)-1-i]:
        is_palindrome = True
    else:
        is_palindrome = False

if is_palindrome:
    print(f"{mot} est un palindrome")
else:
    print(f"{mot} n'est pas un palindrome")


