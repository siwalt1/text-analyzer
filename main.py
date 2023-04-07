import pandas as pd
import numpy as np
import nltk
from nltk.stem import SnowballStemmer

text = "Das ist ein Beispiel Text der analysiert werden soll Dies dient nur zu Testzwecken Beispiele sind toll Analyzen gefallen mir gut"

word_frequency_dictionary = {
    'zu': 0.02,
    'der': 0.15,
    'mir': 0.2,
    'text': 0.03,
    'toll': 0.0025,
    'analyz': 0.00015,
    'gut': 0.23,
    'dies': 0.1,
    'das': 0.3,
    'testzweck': 0.015,
    'beispiel': 0.0094,
    'dient': 0.0022,
    'werd': 0.056,
    'sind': 0.01,
    'soll': 0.025,
    'nur': 0.076,
    'ist': 0.4,
    'gefall': 0.024,
    'ein': 0.03,
    'analysiert': 0.0035,
}



# text to list
list_of_words = text.split(' ')

# Perform tokenization
tokenized_strings = [nltk.word_tokenize(string, "german") for string in list_of_words]

# Perform stemming
stemmer = SnowballStemmer("german")
stemmed_strings = [[stemmer.stem(word) for word in string] for string in tokenized_strings]

# make a simple list of stemmed_strings
list_of_stemmed_words = [word_list[0] for word_list in stemmed_strings]

# count words
individual_words = set(list_of_stemmed_words)
word_frequency = {word: list_of_stemmed_words.count(word) for word in individual_words}

# sort words
sorted_word_frequency = {k: v for k, v in sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)}

# count rare words 
count_rare_words = 0
rare_words = []
for word in sorted_word_frequency:
    if word_frequency_dictionary[word] < 0.01:
        count_rare_words += word_frequency[word]
        rare_words.append(word)

print(count_rare_words)
print(rare_words)