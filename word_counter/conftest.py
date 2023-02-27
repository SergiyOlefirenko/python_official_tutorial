import pytest
from word_counter.wordCounter import WordCounter


@pytest.fixture()
def wc_instance():
    return WordCounter()
