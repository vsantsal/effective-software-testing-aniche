from typing import List


def add(left: List[int], right: List[int]) -> List[int]:
    try:
        left_number: int = _helper_add_converte_lista_para_numero(left)
        right_number: int = _helper_add_converte_lista_para_numero(right)
    except TypeError:
        raise TypeError("'left' and 'right' arguments should be list of integers between 0 and 9!")

    resultado: List[int] = _helper_add_converte_numero_para_lista(left_number + right_number)
    return resultado


def _helper_add_converte_lista_para_numero(lista: List[int]) -> int:
    lista_revertida = list(reversed(lista))
    numero: int = 0
    for i in range(len(lista_revertida)):
        if 0 <= lista_revertida[i] < 10:
            numero += lista_revertida[i]*(10**i)
        else:
            raise ValueError("'left' and 'right' arguments should be list of integers between 0 and 9!")

    return numero


def _helper_add_converte_numero_para_lista(numero: int) -> List[int]:
    comprimento_numero: int = len(str(numero))
    lista: List[int] = [_get_digit(numero, digito) for digito in range(comprimento_numero)]
    return list(reversed(lista))


def _get_digit(numero: int, pos: int) -> int:
    # https://stackoverflow.com/questions/39644638/how-to-take-the-nth-digit-of-a-number-in-python/39644706
    return numero // 10**pos % 10
