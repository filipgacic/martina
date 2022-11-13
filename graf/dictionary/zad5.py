# Dana je datoteka mapa-europa.net u kojoj su zapisani gradovi, avionske
# linije i udaljenosti među gradovima. Spremiti u dictionary gradove i
# udaljenosti na način da je ključ grad, a vrijednost lista uređenih parova
# koji čine grad do kojih postoji let i udaljenost do tog grada. Pritom
# voditi računa da ako postoji linija iz nekog grada u drugi grad, da postoji
# i povratna linija. Napisati funkciju koja za neki grad vraća najbliži i
# najdalji grad do kojeg postoji avionska linija.

with open('/Users/filipgacic/Documents/fax/martina/graf/gradovi.txt') as f:
    dat = f.readlines()
sredeno= []
for i in dat:
    sredeno.append(i.split(' '))

for i in sredeno:
    print(i)
dict = {}

for i in sredeno:
    if(dict[i[0]]):
        dict[i[0]].append((i[1],i[2]))
    dict[i[0]]= [(i[1],i[2])]

print(dict)
