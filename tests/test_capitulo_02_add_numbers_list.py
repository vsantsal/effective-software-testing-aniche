import pytest

from capitulo_02.add_numbers_list import add


@pytest.mark.parametrize('left, right, resultado_esperado',
                         [([], [], [0]),
                          ([9], [], [9]),
                          ([], [0], [0]),
                          ([1, 2], [], [1, 2])])
def test_add_numbers_with_empty_list_argument_use_it_as_zero(left, right, resultado_esperado):
    resultado_obtido = add(left, right)
    assert resultado_obtido == resultado_esperado


@pytest.mark.parametrize('left, right, resultado_esperado',
                         [([5], [4], [9]),
                          ([9], [8], [1, 7]), ])
def test_add_numbers_with_single_digits_works_with_and_without_carry(left,
                                                                     right,
                                                                     resultado_esperado):
    resultado_obtido = add(left, right)
    assert resultado_obtido == resultado_esperado


@pytest.mark.parametrize('left, right, resultado_esperado',
                         [([2, 3], [4, 2], [6, 5]),
                          ([2, 2], [5, 9], [8, 1]),
                          ([5, 5], [9, 9], [1, 5, 4]), ])
def test_add_numbers_with_multiple_digits_works_regardless_of_carry(left,
                                                                    right,
                                                                    resultado_esperado):
    resultado_obtido = add(left, right)
    assert resultado_obtido == resultado_esperado


@pytest.mark.parametrize('left, right, resultado_esperado',
                         [([0, 1], [0, 9], [1, 0]),
                          ([0, 0, 2], [0, 1, 3], [1, 5]), ])
def test_add_numbers_discards_zeroes_to_the_left(left,
                                                   right,
                                                   resultado_esperado):
    resultado_obtido = add(left, right)
    assert resultado_obtido == resultado_esperado


@pytest.mark.parametrize('left, right',
                         [(None, []),
                          ([], None),
                          (None, None),
                          ('a', []),
                          (2, 1),
                          ([], ['a']),
                          ])
def test_add_numbers_raises_type_error_with_unexpected_arguments(left, right):
    with pytest.raises(TypeError) as erro:
        add(left, right)
    assert erro.value.args[0] == "'left' and 'right' arguments should be list of integers between 0 and 9!"


@pytest.mark.parametrize('left, right',
                         [([10], [9]),
                          ([-1], [0]),
                          ([-1], [10]),
                          ([1, -1], [1, 11, 1]),
                          ])
def test_add_numbers_raises_value_error_if_list_has_at_least_one_int_greater_than_9(left, right):
    with pytest.raises(ValueError) as erro:
        add(left, right)
    assert erro.value.args[0] == "'left' and 'right' arguments should be list of integers between 0 and 9!"
