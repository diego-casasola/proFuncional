def pure_integers_sum(number, second_number=2):
    return number + second_number


def pure_integers_res(number, second_number=2):
    return number - second_number


def pure_integers_mul(number, second_number=2):
    return number * second_number


def pure_integers_div(number, second_number=2):
    return number / second_number


# función que reciba de parametro un arreglo y devuelva cada uno de sus elementos elevado a la quinta potencia

def pure_integers_elevator(numbers, potencia):
    result = []
    for number in numbers:
        result.append(number ** potencia)
    return result


def powered(base, power):
    return base ** power


def apply_power_over_list(array, power, function):
    return [function(item, power) for item in array]


# escribir una función que permita filtrar desde un arreglo aquellos elementos que sean impares


def verificar_nro_par(number):
    if number % 2 == 1:
        return number


def nros_pares(array):
    result = []
    for number in array:
        if number % 2 == 1:
            result.append(number)
    return result


def apply_return_pair(array, function):
    return [number for number in array if function(number)]


"""
Módulo de programación funcional en Python
Función MAP --> Aplica una función sobre todos los elementos de un iterable
Función FILTER --> Aplica una función discriminadora sobre todos los elementos del iterable
Función REDUCE --> Retorna el valor acumulado despues de aplicar una función sobre todos los elementos del iterable
"""


def using_map(array, function):
    return list(map(function, array))


# Dado un mensaje devolver la cantidad de palabras presentes en el mensaje, cada una con la cantidad de caracteres

# menseje = 'Hola como estas'
