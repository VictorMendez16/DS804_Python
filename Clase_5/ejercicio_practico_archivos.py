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
        :param columna: Nombre de la columna a imprimir.
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
            if columna == 'colD':
                print(linea.split(',')[3])

    def reescribir_columna_4(self, archivo, numero):
        """
        Reescribe el contenido de la columna 4 del archivo.

        :param archivo: Nombre del archivo.
        """
        self.archivo = open(archivo, 'r')
        self.contenido = self.archivo.readlines()
        nuevo_contenido = ''
        for linea in self.contenido:
            array_linea = linea.split(',')[0:3]
            nueva_linea = f'{array_linea[0]},{array_linea[1]},{array_linea[2]},{numero}\n'
            nuevo_contenido = nuevo_contenido + nueva_linea
        self.archivo.close()

        self.archivo = open(archivo, 'w')
        self.archivo.write(nuevo_contenido)
        self.archivo.close()



""""# Leyendo los argumentos de entrada e instanciando el objecto archivo1
nombre_archivo = argv[1]
columna = argv[2]
archivo1 = Archivos()

print(f'Contenido del archivo')
archivo1.imprimir_contenido(archivo=nombre_archivo)

print(f'Contenido de la columna')
archivo1.imprimir_columna(archivo=nombre_archivo, columna=columna)"""

nombre_archivo = argv[1]
numero = argv[2]
archivo1 = Archivos()

print(f'Contenido del archivo antes de la edicion')
archivo1.imprimir_contenido(archivo=nombre_archivo)
archivo1.reescribir_columna_4(archivo=nombre_archivo, numero=numero)

print(f'\n\nContenido del archivo despues de la edicion')
archivo1.imprimir_contenido(archivo=nombre_archivo)
