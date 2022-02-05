import pytest

from capitulo_03 import count_words_ending_with_r_or_s_in_sentence


def test_count_words_returns_0_given_empty_string():
    number_obtained: int = count_words_ending_with_r_or_s_in_sentence('')
    number_expected: int = 0
    assert number_obtained == number_expected


@pytest.mark.parametrize('word, number_expected',
                         [('abner', 1),
                          ('casas', 1),
                          ('s', 1),
                          ('r', 1),
                          ('a', 0),
                          ('teste', 0)])
def test_count_words_returns_correct_number_for_sentences_with_one_word(word, number_expected):
    number_obtained: int = count_words_ending_with_r_or_s_in_sentence(word)
    assert number_obtained == number_expected


@pytest.mark.parametrize('sentence, number_expected',
                         [('dogs cats', 2),
                          ('dog cat', 0),
                          ])
def test_count_words_returns_correct_number_for_sentences_with_more_words(sentence, number_expected):
    number_obtained: int = count_words_ending_with_r_or_s_in_sentence(sentence)
    assert number_obtained == number_expected


@pytest.mark.parametrize('sentence, number_expected',
                         [('dogs, cats', 2),
                          ('dogs, clear: now is the time - he says.', 4),
                          ])
def test_count_words_returns_correct_number_for_sentences_with_punctuation(sentence, number_expected):
    number_obtained: int = count_words_ending_with_r_or_s_in_sentence(sentence)
    assert number_obtained == number_expected


@pytest.mark.parametrize('wrong_input',
                         [None, 1, [], ])
def test_count_words_raises_type_error_for_wrong_input(wrong_input):
    with pytest.raises(TypeError) as erro_obtido:
        count_words_ending_with_r_or_s_in_sentence(wrong_input)
    assert erro_obtido.value.args[0] == "'sentence' must be 'str'"
