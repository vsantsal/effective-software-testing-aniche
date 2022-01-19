from typing import List, Union


def substrings_between(string: str, beg: str, end: str) -> Union[List[str], str]:
    """

    :param string:
    :param beg:
    :param end:
    :return:
    """
    # lista a ser devolvida pela função
    resultado: List[str] = []
    # se segundo argumento for string vazia, devolve a lista vazia
    if beg == '':
        return resultado
    # tenta obter as posições de beg e end
    # (try/except para possíveis argumentos de outros tipos passados)
    try:
        inicio: int = string.find(beg)
        fim: int = string.find(end)
    except (AttributeError, TypeError):
        raise TypeError("all arguments should be 'str' but were '{}', '{}, '{}'".
                        format(type(string).__name__,
                               type(beg).__name__,
                               type(end).__name__, ))

    while fim > 0:
        nova_substring: str = string[(inicio + len(beg)):fim]
        if len(nova_substring) > 0:
            resultado.append(nova_substring)
        string: str = string[fim + len(end):]
        inicio: int = string.find(beg)
        fim: int = string.find(end)

    return resultado
