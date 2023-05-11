"""
Sets the hex value to a length of two
@hex_value  hexadecimal value in format 0xff
@return str of hex_value
"""


def set_hex(hex_value):
    # Evaluates if number of characters after 0x is equial to 1
    # If it is 1 character long it returns the value with a 0
    # Else it returns de value
    if len(hex_value[2:]) == 1:
        return f"0{hex_value[2:]}"
    else:
        return hex_value[2:]


"""
Evaluates if an integer number is between 0 and 255
@number integer number
"""


def int_number_0_255(number):
    if isinstance(number, int):
        if number >= 0 and number <= 255:
            return True
        else:
            return False
    else:
        return False


"""
Converts integer RGB to hexadecimal RGB
"""


def int_rgb_to_hex_rgb(r, g, b):
    all_integers = int_number_0_255(r) and int_number_0_255(b) and int_number_0_255(b)
    if all_integers:
        hex_r = set_hex(hex(r))
        hex_g = set_hex(hex(g))
        hex_b = set_hex(hex(b))
        hex_rgb1 = f"{hex_r}{hex_g}{hex_b}"
        return hex_rgb1
    else:
        return "Invalid rgb number"


r = 255
g = 125
b = 0

print("Conversion int - hex")
print(f"{r}, {g}, {b} = {int_rgb_to_hex_rgb(r, g, b)}")


def sum_fractions(n1, d1, n2, d2):
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


n1 = 1
d1 = 2
n2 = 3
d2 = 2
print(f"\nSuma de {n1}/{d1} + {n2}/{d2}")
print(sum_fractions(n1, d1, n2, d2))

n1 = 1
d1 = 2
n2 = 2
d2 = 8
print(f"\nSuma de {n1}/{d1} + {n2}/{d2}")
print(sum_fractions(n1, d1, n2, d2))

n1 = 1
d1 = 2
n2 = 2
d2 = 0
print(f"\nSuma de {n1}/{d1} + {n2}/{d2}")
print(sum_fractions(n1, d1, n2, d2))
