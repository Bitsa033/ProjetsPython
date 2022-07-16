print("Programme python  qui calcule et affiche le nombre de voyelles que comporte une phrase")
a = 0
e = 0
i = 0
o = 0
u = 0
y = 0

chaine = input("Entrer une phrase:")
for x in range(0, len(chaine)):
    if chaine[x] == "a":
        a += 1
    elif chaine[x] == "e":
        e += 1
    elif chaine[x] == "i":
        i += 1
    elif chaine[x] == "o":
        o += 1
    elif chaine[x] == "u":
        u += 1
    elif chaine[x] == "y":
        y += 1
print("Taille de la phrase: ", len(chaine))
print("Nom et nombre d'occurences de la voyelle: ")
print("a = ", a)
print("e = ", e)
print("i = ", i)
print("o = ", o)
print("u = ", u)
print("y = ", y)

