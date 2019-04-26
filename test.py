lista = []
f = open(".services.txt")
for linea in f.readlines():
    lista.append(linea)

print(lista)


for x in range(0,len(lista)):
    lista[x] = lista[x][:-1]

print(lista)