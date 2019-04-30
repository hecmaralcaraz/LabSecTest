print(chr(27)+"[1;33m"+"Texto en negrita de color amarillo") 
print("\x1b[1;33m"+"Texto en negrita de color amarillo") 
print("\033[4;35m"+"Texto en negrita y subrayado de color morado") 
print("\033[4;35m""Texto en negrita y subrayado de color morado")
print("\033[1;33m"+"Texto en negrita color amarillo"+'\033[0;m') 
print("\033[;31m"+"Texto normal de color cian")
print("\033[4;35;47m"+"Texto subr morado sobre blanco"+'\033[0;m') 
print("\033[4;31m"+"Texto normal subr color morado"+'\033[0;m')

