from introduction import *

if __name__ == '__main__':
    # print(f'Suma {pure_integers_sum(2)}')
    # print(f'Resta {pure_integers_res(2)}')
    # print(f'Multiplicación {pure_integers_mul(2)}')
    # print(f'División {pure_integers_div(2)}')

    print(f'Elevando números a la quinta potencia: {pure_integers_elevator([1, 5, 7, 3], 5)}')

    array = [1, 2, 4, 6, 8, 9]

    print(f'Solo numeros pares: {nros_pares(array)}')

    print(f'Solo numeros pares con funcion pura: {apply_return_pair(array, verificar_nro_par)}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
