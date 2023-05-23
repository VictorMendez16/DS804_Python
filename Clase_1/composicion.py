import random as rnd

def lectura():
    return rnd.randrange(-10, 100)

def celcius2farenheit(t):
    f = 1.8 * t + 32
    return f
def ajustar(t):
    real = t - 0.5
    return real

def convertir(g, f):
    def h(x):
        return g(f(x))
    return h


temp = -14 #lectura()
print(str(temp)+' C')

conv1 = convertir(ajustar, celcius2farenheit)
temp1 = conv1(temp)
print(temp1)

conv2 = convertir(celcius2farenheit, ajustar)
temp2 = conv2(temp)
print(temp2)


"""temp = ajustar(temp)
print(temp)

temp = celcius2farenheit(temp)
print(temp)"""

def divisor(denominador):
    def dividendo(numerador):
        return numerador/denominador
    return dividendo

division = divisor(2)
print(division(10))
print(division(11))
print(division(12))
print(division(13))
print(division(19))

