# Napisati funkciju koja transponira matricu.

def printMatrica(matrica):
    for i in matrica:
        print(i)

matrica = [[1,2,3],[4,5,6],[6,7,8]]
matrica2 = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(matrica)):
    for j in range(len(matrica[0])):
        matrica2[i][j] = matrica[j][i]
printMatrica(matrica2)
