from sys import argv

class Archivos:
    """ Clase Archivos con metodo para leer e imprimir el contenido de un archivo"""

    def __init__(self):
        """
        Inicia el atributo con el nombre del archivo a utilizar.
        """
        self.archivo = None
        self.contenido = None

    def imprimir_contenido(self, archivo):
        """
        Imprime el contenido del archivo.

        :param archivo: Nombre del archivo.
        """
        self.archivo = open(archivo, 'r')
        self.contenido = self.archivo.read()
        print(self.contenido)
        self.archivo.close()


    def imprimir_columna(self, archivo, columna):
        """
        Imprime el contenido de la columna del archivo.

        :param archivo: Nombre del archivo.
        """
        self.archivo = open(archivo, 'r')
        self.contenido = self.archivo.readlines()
        for linea in self.contenido:
            if columna == 'colA':
                print(linea.split(',')[0])
            if columna == 'colB':
                print(linea.split(',')[1])
            if columna == 'colC':
                print(linea.split(',')[2])

        """if columna == 'colA':
            print((self.contenido[0]).split(',')[0])
        self.archivo.close()"""


# Guardando el nombre del archivo en una variable e instanciando el objeto archivo1
nombre_archivo = 'ejemplo.csv'
archivo1 = Archivos()

print('Contenido del archivo')
archivo1.imprimir_contenido(archivo=nombre_archivo)

print('Contenido de la columna A')
archivo1.imprimir_columna(archivo=nombre_archivo, columna='colA')

print('Contenido de la columna B')
archivo1.imprimir_columna(archivo=nombre_archivo, columna='colB')

print('Contenido de la columna C')
archivo1.imprimir_columna(archivo=nombre_archivo, columna='colC')

print(type(argv))
print(argv)
