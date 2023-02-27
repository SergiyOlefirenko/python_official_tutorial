def test_add_word(wc_instance):
    wc_instance.add_word('apple')
    assert wc_instance.words['apple'] == 1
    wc_instance.add_word('apple')
    assert wc_instance.words['apple'] == 2

def test_add_word_case_insensitiveness(wc_instance):
    wc_instance.add_word('Apple')
    assert wc_instance.words['apple'] == 1

def test_get_count_positive(wc_instance):
    wc_instance.add_word('apple')
    assert wc_instance.get_count('Apple') == 1

def test_get_count_negative(wc_instance):
    assert wc_instance.get_count('banana') == 0
