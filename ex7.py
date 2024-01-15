# const arr = ['a','b','a','b','d','a','a','b','f','a'];
# Trouver et compter l'élément qui existe le plus de fois dans le tableau.

arr = ['a', 'b', 'a', 'b', 'd', 'a', 'a', 'b', 'f', 'a']
countDict = {}

for l in arr:
    if l in countDict:
        countDict[l] += 1
    else:
        countDict[l] = 1

greatestKey = ''
greatestValue = 0

for k, v in countDict.items():
    if v > greatestValue:
        greatestValue = v
        greatestKey = k
