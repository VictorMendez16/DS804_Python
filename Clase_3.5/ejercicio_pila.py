class Pila:
    """ Clase Pila con metodos de agregar, eliminar, buscar e imprimir. """

    def __init__(self, *args):
        """
        Crea una pila vacía.

        :param *args: Elementos con los cuales inicializar la pila.
        """
        # La pila vacía se representa con una lista vacía
        self.elementos = [*args]

    def agregar(self, elemento):
        """
        Agrega el elemento a la pila.

        :param elemento: Elemento a agregar a la pila.
        """
        # Agrega al final de la lista.
        self.elementos.append(elemento)

    def eliminar(self):
        """
        Elimina el ultimo elemento de la pila. Si la pila está vacía levanta una excepción.

        :return: Elemento eliminado.
        """
        try:
            return self.elementos.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def buscar(self, busca_elemento):
        """
        Busca el elemento dentro de la pila y devuelve su posicion.

        :param busca_elemento: Elemento a buscar.
        :return: Inidice en el se encuentra el elemento. None si no se encuentra.
        """
        contador = 0
        for elemento in self.elementos:
            if elemento == busca_elemento:
                return contador
            contador += 1
        return None

    def imprimir(self):
        """
        Imprime los elementos de la pila.
        """
        for elemento in self.elementos:
            print(elemento)


# Creando una pila e imprimiendola
print('Crear la pila')
pila = Pila('Elemento1', 'Elemento2', 'Elemento3')
pila.imprimir()
print()

# Agregar un elemento a la pila e imprimir la pila resultante
print('Agregar un elemento a la pila e imprimir la pila resultante')
pila.agregar('Elemento agregado')
pila.imprimir()
print()

# Elimina un elemento de la pila e imprimir la pila resultante
print('Eliminar un elemento de la pila e imprimir la pila resultante')
pila.eliminar()
pila.imprimir()
print()

# Buscando un elemento en la pila
elemento_a_buscar = 'Elemento3'
print(f'Buscar el elemento {elemento_a_buscar} en la pila e imprimir la pila')
print(pila.buscar(busca_elemento=elemento_a_buscar))
pila.imprimir()

