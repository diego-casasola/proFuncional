from introduction import *
from practico import *

if __name__ == '__main__':
    # print(f'Suma {pure_integers_sum(2)}')
    # print(f'Resta {pure_integers_res(2)}')
    # print(f'Multiplicación {pure_integers_mul(2)}')
    # print(f'División {pure_integers_div(2)}')

    # print(f'Elevando números a la quinta potencia: {pure_integers_elevator([1, 5, 7, 3], 5)}')
    #
    # array = [1, 2, 4, 6, 8, 9]
    #
    # print(f'Solo numeros pares: {nros_pares(array)}')
    #
    # print(f'Solo numeros pares con funcion pura: {apply_return_pair(array, verificar_nro_par)}')


    print('---')

    a  = [21, 27, 23, 20, 21, 25, 15]
    b= [8, 46, 45, 49, 15, 6, 31]
    # print(f'Mayores a 22: {get_num(a)}')
    print(f'suma de valores mayores a 22: {suma_all(a, get_num)}')
    print(f'suma de valores mayores a 22: {suma_all(b, get_num)}')

    print('---------------------------')
    print(f'Aplicar IVA: {apply_iva_price_list(a, apply_iva)}')
    print(f'Aplicar IVA: {sum_precios(b, apply_iva_price_list,apply_iva)}')

    print('---------------------------')
    print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
