# Iz dictionaryja čiji su ključevi brojevi, a vrijednosti liste brojeva, 
# napravite drugi dictionary čiji će ključevi biti jednaki kao u prvom, 
# a vrijednosti će biti duljine lista koje su bile vrijednosti odgovarajućih ključeva
# u prvom dictionaryju.

dict={1:[2,3,4],2:[4,5,6,7]}

dict2 = {}

for i in dict:
    dict2[i] = len(dict[i])

print(dict2)