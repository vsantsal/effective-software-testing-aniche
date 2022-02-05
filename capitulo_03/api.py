from string import punctuation


def count_words_ending_with_r_or_s_in_sentence(sentence: str) -> int:
    try:
        target_words_count: int = sum(1 for word
                                      in sentence.split()
                                      if word.rstrip(punctuation).endswith(('r', 's')))
    except AttributeError:
        raise TypeError("'sentence' must be 'str'")
    return target_words_count
