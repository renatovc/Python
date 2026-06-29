import csv
from collections import Counter

INVALID_TYPES = ["Adverb", "Adverb et al.", "Adverb, preposition",
 "Adverb, preposition, et al.", "Adverb, pronoun, et al.",
 "Article", "Coordinator", "Coordinator, adverb, et al.",
 "Determiner", "Determiner, adverb", "Determiner, adverb, noun",
 "Possessive pronoun", "Preposition",
 "Preposition, adverb, coordinator", "Preposition, adverb, et al.",
 "Pronoun", "Pronoun, adverb, et al.", "Pronoun, noun",
 "Subordinator, determiner"]


def get_word_frequency(text, INVALID_TYPES):
    with open('common_words.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        palabras_comunes = [row for row in reader]

    words = get_words(text)

    filtered_words = [word for word, _ in palabras_comunes if word not in INVALID_TYPES]

    word_counter = Counter(words)

    valid_words = []
    frequencies = []
    for word in filtered_words:
        valid_words.append(word)
        frequencies.append(word_counter[word])

    return [valid_words, frequencies]

def get_words(text):
    words = text.lower().split()
    words = [word.strip('.,?!";()') for word in words]
    return words

def get_most_frequent(words, frequencies, n=10):
  sorted_pairs = sorted([(word, freq) for word, freq in zip(words, frequencies)], key=lambda x: (x[1], x[0]), reverse=True)
  top_n_pairs = sorted_pairs[:n]
  top_n_words, top_n_frequencies = [list(pair) for pair in zip(*top_n_pairs)]
  return [top_n_words, top_n_frequencies]