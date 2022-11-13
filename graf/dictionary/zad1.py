# Napisati funkciju koja iz matrice a takve da je A[i][j]=w kreira dictionary
# u kojem su oznake redaka i ključevi, a vrijednosti lista uređenih parova
# (j, w) za svaki j za koji je w razlicit od 0

def printMatrica(matrica):
    for i in matrica:
        print(i)

matrica = [[1,2],[4,5],[6,7]]
printMatrica(matrica)

dict = {}
for i in range(len(matrica)):
    for j in range(len(matrica[0])):
        dict[i] = (j,matrica[i][j])

print(dict)



