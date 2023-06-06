"""
Programa que defina números complejos en sus representación binómica y sus operaciones básicas de:
• Imprimir
• Multiplicación por escalar
• Módulo
• Conjugación
"""

# Importacion de metodo para calcular raiz cuadrada
from math import sqrt

# Definicion de clase NumeroComplejo
class NumeroComplejo:
    """ Clase NumeroComplejo."""

    # Atributos
    def __init__(self, parte_real, parte_imag):
        self.parte_real = parte_real
        self.parte_imag = parte_imag

    # Metodos
    def multiplicacion_escalar(self, escalar):
        """
        Multiplica el numero complejo por un escalar y actualiza los atributos.

        :param escalar: Numero a multiplicar por el numero complejo.
        :return: Cadena del numero complejo resultante
        """
        self.parte_real = self.parte_real * escalar
        self.parte_imag = self.parte_imag * escalar
        return f"{self.parte_real} + {self.parte_imag}i"

    def modulo(self):
        """
        Calcula el modulo del numero complejo

        :return: Modulo resultante
        """
        return sqrt((self.parte_real**2)+(self.parte_imag**2))

    def conjugado(self):
        """
        Calcula el conjugado del numero complejo y actualiza los atributos

        :return: Cadena del conjugado resultante
        """
        self.parte_imag = - self.parte_imag
        if self.parte_imag < 0:
            return f'{self.parte_real} {self.parte_imag}i'
        elif self.parte_imag >= 0:
            return f'{self.parte_real} + {self.parte_imag}i'

    def imprimir_binomica(self):
        """
        Imprime el numero complejo en su formato binomico.

        :return: Cadena del numero complejo en su formato binomico
        """
        if self.parte_imag < 0:
            return f'{self.parte_real} {self.parte_imag}'
        elif self.parte_imag >= 0:
            return f'{self.parte_real} + {self.parte_imag}i'

# Declarando un numero complejo
numero_comlejo = NumeroComplejo(3, 1.5)


# Imprimiendo la representacion binomica del numero complejo
print('Impresion del numero complejo en representacion binomica')
print(numero_comlejo.imprimir_binomica())

# Imprimiendo la multiplicacion del numero complejo por un escalar
escalar = 2
print(f'Impresion del numero complejo multiplicado por el escalar {escalar}')
print(numero_comlejo.multiplicacion_escalar(escalar=escalar))

# Imprimiendo el modulo del numero complejo
print('Impresion del modulo del numero complejo')
print(numero_comlejo.modulo())

# Imprimiendo el conjugado del numero complejo
print('Impresion del conjugado del numero complejo')
print(numero_comlejo.conjugado())
