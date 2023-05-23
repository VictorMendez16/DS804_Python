def fun1(msg):
    print(msg)


def fun2(msg):
    return msg + '!'


fun1('Hola')
print(fun2('Hola'))
fulanito = fun1
print(type(fulanito))


def suma(*numeros):  # Espera argumentos anonimos
    acumulador = 0;
    for numero in numeros:
        acumulador += numero
    return acumulador


r = suma(1, 1, 2, 3)
print(r)

def operacion(n1, n2, **args):
    # Suma n1 y n2
    # En caso de existir n3 multiplicar r por n3
    r = n1 + n2
    if 'n3' in args:
        r = r * args['n3']
    return r

r = operacion(1, 1, n3=2, n4=3)
print(r)

"""def suma(**numeros):  # Espera argumentos nombrados y no anonimos
    acumulador = 0
    print(n4)
    for numero in numeros:
        print(numero)
        acumulador += numero
    return acumulador


r = suma(n1=1, n2=1, n3=2, n4=3)
print(r)"""

def f1(x):
    def f2(y):
        return (y+1)
    while x < 100:
        x += f2(x)
