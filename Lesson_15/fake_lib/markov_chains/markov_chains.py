"""
This function takes text with real data (firstnames, lastnames,
email addresses, etc.) as an argument and returns a dictionary with tokens
based on that data, where the values are lists of possible tokens. This
dictionary can be used in an algorithm to generate non-existent
(and sometimes existing), but more or less readable human text values using a
process such as "Markov chains".
"""

from .file_utils import get_file_path


def generate_tokens(file: str) -> dict:
    tokens = dict()
    with open(file) as file:
        file = file.read().splitlines()
        for row in file:
            for index, letter in enumerate(row):
                if letter not in tokens and index != len(row)-1:
                    tokens[letter] = [row[index+1]]
                elif index != len(row)-1:
                    tokens[letter].append(row[index+1])
    return tokens


first_names_tokens = generate_tokens(get_file_path('firstnames.txt'))
last_names_tokens = generate_tokens(get_file_path('lastnames.txt'))
emails_tokens = generate_tokens(get_file_path('emails.txt'))
