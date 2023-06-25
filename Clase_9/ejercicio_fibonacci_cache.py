"""
Comparacion de ejecucion del mismo metodo con y sin el decorador cache
"""

from functools import cache
import time


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

@cache
def fibonacci_cache(numero):
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
        return fibonacci_cache(numero - 1) + fibonacci_cache(numero - 2)


numero = int(input("Numero entero para calcular el ensemimo valor de la serie de Fibonacci: "))
calculos = int(input("Numero de veces que desa hacer el calculo: "))

# Sin el decorador cache
tiempo_de_inicio = time.time()
fibonacci(numero)
tiempo_final = time.time()
tiempo_de_ejecucion = tiempo_final - tiempo_de_inicio

print(f"\nCalculo de fibonacci({numero}) sin cache")
print(f"Tiempo de ejecucion sin cache: {tiempo_de_ejecucion} segundos")

# Utilizando el decorador cache
for i in range(calculos):
    tiempo_de_inicio = time.time()
    fibonacci_cache(numero)
    tiempo_final = time.time()
    tiempo_de_ejecucion = tiempo_final - tiempo_de_inicio

    print(f"\nCalculo {i+1} de fibonacci({numero})")
    if i == 0:
        # Al momento de ejecutar fibonacci_cache() por primeravez no hay ningun resultado previamente almacenado
        # cache y realiza n llamadas recursivas
        print(f"Tiempo de ejecucion sin cache: {tiempo_de_ejecucion} segundos")
    else:
        # Al momento de vovler a ejecutar fibonacci_cache() busca el resultado del valor en caché resultando en
        # un menor tiempo de ejecucion
        print(f"Tiempo de ejecucion con cache: {tiempo_de_ejecucion} segundos")
