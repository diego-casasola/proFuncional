from functools import reduce

"""
Ejercicio 1
"""
def get_num(array):
    return [number for number in array if number <= 22]


def suma_all(array, function):
    return sum(function(array))


"""
Ejercicio 2
"""

def apply_iva(precio):
    return precio + ((precio * 13) / 100)

def apply_iva_price_list(array, function):
    return list(map(function, array))

def sum_precios(array, function, function2):
    return sum(number for number in function(array,function2))


"""
Ejercicio 3
"""

def obtener_palabras(message):
    return message.split()



