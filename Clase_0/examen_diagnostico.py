"""
Examen diagnostico de Python.
"""

def set_hex(hex_value):
    """
    Evalua un numero en formato hexadecimal y lo regresa en formato 0xff.

    :param hex_value: numero hexadecimal.
    :return: numero en formato 0xff.
    """
    if len(hex_value[2:]) == 1:
        return f"0{hex_value[2:]}"
    else:
        return hex_value[2:]


def int_number_0_255(number):
    """
    Evalua si un numero esta entre 0 y 255.

    :param number: numero entero.
    :return: True si esta entre 0 y 255 y False en caso contrario.
    """
    if isinstance(number, int):
        if number >= 0 and number <= 255:
            return True
        else:
            return False
    else:
        return False


def int_rgb_to_hex_rgb(r, g, b):
    """
    Convierte valores enteros de RGB a sus equivalentes en hexadecimal.

    :param r: Numero entero del valor Red.
    :param g: Numero entero del valor Blue.
    :param b: Numero entero del valor Green.
    :return: Cadena de los valores RGB en formato hexadecimal.
    """
    all_integers = int_number_0_255(r) and int_number_0_255(b) and int_number_0_255(b)
    if all_integers:
        hex_r = set_hex(hex(r))
        hex_g = set_hex(hex(g))
        hex_b = set_hex(hex(b))
        hex_rgb1 = f"{hex_r}{hex_g}{hex_b}"
        return hex_rgb1
    else:
        return "Invalid rgb number"

# Declarando valores RGB
r = 255
g = 125
b = 0

# Imprimiendo los valores RGB en formato hexadecimal
print("Conversion int - hex")
print(f"{r}, {g}, {b} = {int_rgb_to_hex_rgb(r, g, b)}")


def sum_fractions(n1, d1, n2, d2):
    """
    Suma dos fracciones.

    :param n1: Numerador de la primera fraccion.
    :param d1: Denominador de la primera fraccion.
    :param n2: Numerador de la segunda fraccion.
    :param d2: Denominador de la segunda fraccion.
    :return: Cadena com el resultado de la suma de la fraccion 1 con la fraccion 2.
    """
    if d1 == 0 or d2 == 0:
        return "A denominator is 0"
    else:
        if d1 == d2:
            num = n1 + n2
            den = d1

        else:
            den = d1 * d2
            num = (n1 * d2) + (n2 * d1)

        r = f"{num}/{den}"
        return r

# Declarando la fraccion 1 y fraccion 2
n1 = 1
d1 = 2
n2 = 3
d2 = 2

# Imprimiendo la suma de la fraccion 1 con la fraccion 2
print(f"\nSuma de {n1}/{d1} + {n2}/{d2}")
print(sum_fractions(n1, d1, n2, d2))

# Reasignando la fraccion 1 y fraccion 2
n1 = 1
d1 = 2
n2 = 2
d2 = 8

# Imprimiendo la suma de la fraccion 1 con la fraccion 2
print(f"\nSuma de {n1}/{d1} + {n2}/{d2}")
print(sum_fractions(n1, d1, n2, d2))


# Reasignando la fraccion 1 y fraccion 2
n1 = 1
d1 = 2
n2 = 2
d2 = 0

# Imprimiendo la suma de la fraccion 1 con la fraccion 2
print(f"\nSuma de {n1}/{d1} + {n2}/{d2}")
print(sum_fractions(n1, d1, n2, d2))
