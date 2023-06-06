"""Ejercicio 1: Serie de Fibonacci haciendo uso de recursividad."""


def fibonacci(numero):
    """
    Calcula el enesimo valor de la serie de Fibonacci.

    :param numero: Enesimo valor a calcular de la serie de Fibonacci.
    :return: Enesimo valor calculado de la serie de Fibonacci.
    """
    # Si el numero es 1 o menor regresa el mismo numero.
    if numero <= 1:
        return numero
    # Si el numero es mayor a 1 se llama a si mismo con el argumento anterior y el anterior a este.
    # Regresa la suma de estos valores para calcular el enesimo valor.
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)


enesimo_valor = 8  # Enesimo valor dela serie.
print(f'El valor {enesimo_valor} de la serie de Fibonacci es {fibonacci(enesimo_valor)}')  # Imprime el resultado.


"""Ejercicio 2: Tomar un valor flotante, obtener su cuadrado y convertirlo a entero usando la tecnica de composicion."""


def cuadrado(numero):
    """
    Calcula el cuadrado de un numero.

    :param numero: Numero al cual se le calcula su cuadrado.
    :return: Numero al cuadrado.
    """
    return pow(numero, 2)


# La funicion toma un valor flotante y lo convierte a entero
def float2int(numero):
    """
    Convierte un numero flotante a entero.

    :param numero: Numero a convertir en entero.
    :return: Numero entero
    """
    return int(numero)


def cuadradoEntero(g, f):
    """
    Funcion compuesta donde evalua h(x) = g(f(x)) y regresa h. Obtiene un numero flotante, lo eleva al cuadrado
    y regresa el numero en entero

    :param g: funcion g.
    :param f: funcion f.
    :return: Evaluacion de h(x) = g(f(x)).
    """
    def h(x):
        return g(f(x))

    return h


numero = 3.3  # Numero a calcular su cuadrado entero.
operacion = cuadradoEntero(float2int, cuadrado)  # Implementando la tecnica de composicion.
resulatdo = operacion(3.3)  # Llamando la funcion compuesta para calcular el cuadrado entero.
print(f'El cuadrado entero de {numero} es {resulatdo}')
