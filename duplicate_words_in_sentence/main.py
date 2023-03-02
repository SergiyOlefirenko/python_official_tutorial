sentence = 'a girs has a Cat cat who was was very bad bad cat'
result = {}
words = sentence.lower().split()

for word in set(words):
    if words.count(word) > 1:
        result[word] = words.count(word)
        print(f'Word "{word}" has {result[word]} duplicates in the inputted sentence.')

print(f'{result=}')

from collections import Counter

word_counts = Counter(sentence.lower().split())
print(word_counts)

for word, count in word_counts.items():
    if count > 1:
        print(f'{word}: {count} times')
