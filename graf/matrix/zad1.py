def printMatrica(matrica):
    for i in matrica:
        print(i)





with open('/Users/filipgacic/Documents/fax/martina/graf/gradovi.txt') as f:
    dat = f.readlines()
ocisceno = []
for i in dat:
    ocisceno.append(i.split(' '))

gradovi = []
for i in ocisceno:
    if i[0] not in gradovi: 
        gradovi.append(i[0])

    if i[1] not in gradovi: 
        gradovi.append(i[1])    

matrica = []

for i in range(len(gradovi) + 1):
    red = []
    for j in range(len(gradovi)+1):
        red.append(0)
    matrica.append(red)

for i in range(len(gradovi)):
    matrica[i+1][0] = gradovi[i]
    matrica[0][i+1] = gradovi[i]

for i in ocisceno:
    matrica[matrica[0].index(i[1])][matrica[0].index(i[0])] = i[2]
    matrica[matrica[0].index(i[0])][matrica[0].index(i[1])] = i[2]

printMatrica(matrica)












