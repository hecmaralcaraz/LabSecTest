lista = []
serv = [1,2,3,4]

for i in range(0,len(serv)):
    if serv[i] == 1:
        lista.append('DHCP')
    if serv[i] == 2:
        lista.append('DNS')

print(lista)