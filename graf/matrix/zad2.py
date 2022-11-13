# Napisati funkciju koja provjerava je li neka matrica kvadratna, drugu
# koja provjerava je li simetrična, treću koja provjerava je li matrica
# stohastička po stupcima (suma elemenata svakog stupca je 1).
def printMatrica(matrica):
    for i in matrica:
        print(i)

matrica = []

for i in range(7):
    red = []
    for j in range(7):
        red.append(0)
    matrica.append(red)






if(len(matrica)==len(matrica[0])):
    print('da')


for i in range(len(matrica)):
    for j in range(len(matrica[0])):
        if(matrica[i][j]!= matrica[j][i]):
            print('nije')
            
print('je')
# printMatrica(matrica)
