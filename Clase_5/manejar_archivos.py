archivo1 = open('archivo.txt', 'r')
print('Tipo de dato: ' + str(type(archivo1)))
print(archivo1)

contenido1 = archivo1.read()
print('Tipo de dato del contenido: ' + str(type(contenido1)))
print(contenido1)

archivo1.close()

archivo1 = open('archivo.txt', 'r')
contenido2 = archivo1.read()
print('Contenido 2:' + contenido2)
archivo1.close()

with open('archivo.txt', 'w') as archivo:
    archivo.write("Linea 1\n")

with open('archivo.txt', 'a') as archivo:
    archivo.write("Linea 2\n")

with open('archivo.txt', 'a') as archivo:
    archivo.write("Linea 3\n")

archivo1 = open('archivo.txt', 'r')
contenido1 = archivo1.read()
print('Contenido del archivo:\n' + contenido1)
archivo1.close()
