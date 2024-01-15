# Votre programme consistera à demander à l’utilisateur de rentrer successivement
# deux valeurs (chaines de caractères) et de vérifier si ces deux valeurs sont
# identiques ou non.
# Vous afficherez un message pour donner la réponse de cette comparaison.

def compare(value1, value2):
    if value1 == value2:
        print(f"Les deux chaines sont identiques : ({value1} et {value2})")
    else:
        print(f"Les deux chaines ne sont paas identiques : ({value1} et {value2})")

print("saisir valeur 1 :")
val1 = input()

print("saisir valeur 2 :")
val2 = input()

compare(val1, val2)