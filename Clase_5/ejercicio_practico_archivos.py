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


# Leyendo los argumentos de entrada e instanciando el objecto archivo1
nombre_archivo = argv[1]
columna = argv[2]
archivo1 = Archivos()

print(f'Contenido del archivo')
archivo1.imprimir_contenido(archivo=nombre_archivo)

print(f'Contenido de la columna')
archivo1.imprimir_columna(archivo=nombre_archivo, columna=columna)
