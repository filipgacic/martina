# Napisati funkciju koja računa zbroj elemenata na glavnoj dijagonali i zbroj
# elemenata na sporednoj dijagonali. Ako matrica nije kvadratna, funkcija
# baca iznimku.

matrica = []

for i in range(7):
    red = []
    for j in range(7):
        red.append(0)
    matrica.append(red)
matrica[2][2] = 1
matrica[1][6]=3

suma = 0
for i in range(len(matrica)):
    suma = suma + matrica[i][i]

print(suma)

sumaSporedne = 0
for i in range(len(matrica)):
    sumaSporedne = sumaSporedne + matrica[i][len(matrica)-1]

print(sumaSporedne)