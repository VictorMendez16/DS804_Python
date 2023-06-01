tupla1 = ()
print(type(tupla1))
tupla2 = (['a', 'b', 'c'])
print(tupla2)

# Conjuntos
# Un objecto es hashable si tiene un valor de hash que nunca cambiara
# El set puede cambiar
# Un set no esta indexado ni ordenado
set1 = {'a', 'b', 'c'}
print(type(set1))
set1.remove('a')

set2 = frozenset({'a', 'b', 'c'})
print(type(set2))
# set1.remove('a')  # Los frozensets no pueden ser modificados add/remove como los set normales

# Diccionarios
# Son de tipo maping que relaciona valores con objetos de cualquier tipo
a = 24
b = 'Hola mundo'
c = ['.', 'o', ';']
tupla = a, b, c
print(type(tupla))
print(tupla)

set0 = a, b
print(type(set0))
print(set0)

d1 = {'a': a, 'b': 'Hola mundi', 'c': c}
print(d1)
