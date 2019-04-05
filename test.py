import os
os.system('ls sdhndfxymjnxfs.NOEXISTE')
os.system('echo $?')  # mostra 0 en lloc d'un altre nombre com hauria de mostrar al fallar la comanda 'ls' anterior.

# L'objectiu es comprovar si una comanda falla o no.
# PD: Jo també m'he viciat a utilitzar vim.
