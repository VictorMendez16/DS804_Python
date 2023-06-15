def busqueda_binaria(lista, valor):
    """
    Busca un valor dentro de una lista ordenada
    :param lista_ordenada: Lista de valores ordenados
    :param valor: Valor a buscar en la lista
    :return: Indice de posicion del valor en la lista o None si el valor no esta en la lista
    """

    lista.sort()
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        pivote = (izquierda + derecha)//2

        if lista[pivote] == valor:
            return pivote
        if lista[pivote] > valor:
            derecha = pivote - 1
        if lista[pivote] < valor:
            izquierda = pivote + 1


lista = [1, 2, 3, 4, 5, 6]
valor = 3
indice = busqueda_binaria(lista=lista, valor=17)
print(f"El valor {valor} se encuentra en el indice {indice} de la lista {lista}")

lista = [6, 4, 1, 3, 2, 5]
valor = 3
indice = busqueda_binaria(lista=lista, valor=17)
print(f"El valor {valor} se encuentra en el indice {indice} de la lista {lista}")

