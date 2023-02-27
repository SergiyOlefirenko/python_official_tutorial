class WordCounter():

    def __init__(self) -> None:
        self.words = {}

    def add_word(self, word: str):
        word = word.lower()
        if self.words.get(word, None):
            self.words[word] += 1
        else:
            self.words[word] = 1

    def get_count(self, word: str) -> int:
        return self.words.get(word.lower(), 0)


if __name__ == '__main__':
    wc = WordCounter()

    wc.add_word('apple')
    wc.add_word('banana')
    wc.add_word('apple')

    assert wc.get_count("apple") == 2
    assert wc.get_count("banana") == 1
    assert wc.get_count("orange") == 0
