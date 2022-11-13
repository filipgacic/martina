# Napisati funkciju koja generira dictionary na sljedeći način. Za dani
# prirodan broj n ključevi su brojevi između 1 i n. 
from random import randint

lista = [5,7,3,55]

dict = {}

for i in lista:
    dict[i] = randint(0,i)

print(dict)



