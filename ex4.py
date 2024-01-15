# Créer un algorithme qui retourne la valeur la plus haute dans un tableau.
# arr = [10,12,1,3,523,100,43,23]; // Renverra 523

arr = [10,12,1,3,523,100,43,23]

# print(len(arr))
max = arr[0]
for n in arr:
    if n > max:
        max = n

print(f"maxi : {max} ")




