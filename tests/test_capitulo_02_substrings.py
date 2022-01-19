import pytest

from capitulo_02.substrings import substrings_between


@pytest.mark.parametrize('texto, texto_inicio, texto_fim, saida_esperada',
                         [('axcaycazc', 'a', 'c', ['x', 'y', 'z']),
                          ('abcdabcdab', 'a', 'd', ['bc', 'bc']),
                          ('aabcddaabfddaab', 'aa', 'dd', ['bc', 'bf']),
                          ])
def test_substrings_between_retorna_string_com_intervalos_particionados_corretamente(texto,
                                                                                     texto_inicio,
                                                                                     texto_fim,
                                                                                     saida_esperada):
    saida_obtida = substrings_between(texto, texto_inicio, texto_fim)
    assert saida_obtida == saida_esperada


@pytest.mark.parametrize('texto, texto_inicio, texto_fim',
                         [('', 'a', 'c'),
                          ('', '', ''),
                          ('abc', '', ''),
                          ('abc', '', 'c'),
                          ('abc', 'a', ''),
                          ('a', 'a', 'a'),
                          ('a', 'a', 'b'),
                          ('a', 'b', 'a'),
                          ('a', 'x', 'y'),
                          ('aabb', 'aa', 'bb'),
                          ])
def test_substrings_between_retorna_lista_vazia_para_casos_acordados(texto,
                                                                     texto_inicio,
                                                                     texto_fim):
    saida_obtida = substrings_between(texto, texto_inicio, texto_fim)
    assert saida_obtida == []


@pytest.mark.parametrize('entrada',
                         [None,
                          3.2,
                          1,
                          0,
                          ('abc',),
                          ['abc', ]])
def test_substrings_between_lanca_type_error_para_string_nao_str(entrada):
    with pytest.raises(TypeError) as erro:
        substrings_between(entrada, 'a', 'c')
    assert erro.value.args[0] == "all arguments should be 'str' but were '{}', '{}, '{}'". \
        format(type(entrada).__name__,
               type('a').__name__,
               type('c').__name__, )


@pytest.mark.parametrize('entrada',
                         [None,
                          3.2,
                          1,
                          0,
                          ('abc',),
                          ['abc', ]])
def test_substrings_between_lanca_value_error_para_beg_nao_str(entrada):
    with pytest.raises(TypeError) as erro:
        substrings_between('abc', entrada, 'c')
    assert erro.value.args[0] == "all arguments should be 'str' but were '{}', '{}, '{}'". \
        format(type('abc').__name__,
               type(entrada).__name__,
               type('c').__name__, )


@pytest.mark.parametrize('entrada',
                         [None,
                          3.2,
                          1,
                          0,
                          ('abc',),
                          ['abc', ]])
def test_substrings_between_lanca_value_error_para_end_nao_str(entrada):
    with pytest.raises(TypeError) as erro:
        substrings_between('abc', 'a', entrada)
    assert erro.value.args[0] == "all arguments should be 'str' but were '{}', '{}, '{}'". \
        format(type('abc').__name__,
               type('a').__name__,
               type(entrada).__name__, )
