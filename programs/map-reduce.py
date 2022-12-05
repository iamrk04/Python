def count_words(doc):
    normalized_doc = ''.join(char.lower() if char.isalpha() else ' ' for char in doc)
    frequencies = {}
    for word in normalized_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

docs = [
    "It was the best of times, it was the worst of times.",
    "I went to Ooty becuase it was not cold over there then.",
    "I love ice cream.",
    "I do not like fake people."
]

counts = map(count_words, docs)


def combine_counts(d1, d2):
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d

from functools import reduce
total_counts = reduce(combine_counts, counts)
print(total_counts)