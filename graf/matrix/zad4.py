# Napisati funkciju koja računa umnožak matrica i drugu koja računa zbroj.
# Ako dimenzije matrica nisu ispravne, funkcije bacaju iznimke.
def printMatrica(matrica):
    for i in matrica:
        print(i)

def pomnoziListu(lista):
    produkt = 1
    for i in lista:
        produkt = produkt * i
    return produkt

def pomnoziStupad(matrica,red):
    produkt = 1
    for i in matrica:
        produkt = produkt * i[red]
    return produkt

matrica = [[1,2],[2,3]]
matrica2 = [[2,3,4],[5,6,7]]
matrica3 = []

for i in range(len(matrica)):
    red = []
    for j in range(len(matrica2[0])):
        red.append(0)
    matrica3.append(red)
if(len(matrica[0])==len(matrica2)):
    for i in range(len(matrica)):
        for j in range(len(matrica2[0])):
            matrica3[i][j]=pomnoziListu(matrica[i]) + pomnoziStupad(matrica2,j)
    
    
    
printMatrica(matrica3)



