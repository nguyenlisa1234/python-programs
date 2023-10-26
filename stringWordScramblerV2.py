# Homework 9
# White Python
# 10/25/2023


import random 

def word_count_limits(word):
    vowel_replacements = {
        'a': ('e', 'i', 'o', 'u'),
        'i': ('a', 'e', 'o', 'u'),
        'y': ('a', 'e','i','o','u')
    }
    if len(word) == 1:
        if word.lower() in vowel_replacements:
            random_vowel = random.choice(vowel_replacements[word.lower()])
            return random_vowel.upper() if word.isupper() else random_vowel
    elif len(word) == 2:
        scrambled_word = ""
        for i in word:
            scrambled_word = i + scrambled_word
        return scrambled_word
    else:
        scrambled_word = ""
        for i in word:
            scrambled_word = i + scrambled_word
        return scrambled_word

def even_odd_words(word):
    if len(word) > 3:
        if len(word) % 2 == 0:
            even = word[1:-1]
            rotated_even = even[-1] + even[:-1]
            return word[0] + rotated_even + word[-1]
        else:
            middle_letters = list(word[1:-1])
            random.shuffle(middle_letters)
            return word[0] + ''.join(middle_letters) + word[-1]
    else:
        return word

def word_scrambler(word):
    if len(word) > 3:
        return even_odd_words(word)
    else:
        return word_count_limits(word)



def final_message(message):
    words = message.split()
    scrambled_words = []
    scrambled_words_set = []
    punctuation = {',', '.', '?', '!', "'", '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', ';', '<', '>', '/', '|', '[', ']', '{', '}', '+', '=', '`', '~'}
    apostrophe = {"'s", "'t", "'d", "'m", "'re", "'ve", "'ll", "'all", "'t"}

    for word in words:
        if ':' in word: # deals with cases with time
            colon_position = word.find(":")
            before_colon = word[:colon_position]
            after_colon = word[colon_position + 1:]
            scrambled_before_colon = word_scrambler(before_colon)
            scrambled_after_colon = word_scrambler(after_colon)
            scrambled_word = f'{scrambled_before_colon}:{scrambled_after_colon}'
        elif "'" in word and word in apostrophe: # deals with apostrophes so that everyting after the apostrophe does not mix
            apostrophe_position = word.find("'")
            before_apostrophe = word[:apostrophe_position]
            after_apostrophe = word[apostrophe_position + 1:]
            scrambled_before_apostrophe = word_scrambler(before_apostrophe)
            scrambled_word = f"{scrambled_before_apostrophe}'{after_apostrophe}"
        elif "'" in word: # deals with apostrophes not stated
            apostrophe_position = word.find("'")
            before_apostrophe = word[:apostrophe_position]
            after_apostrophe = word[apostrophe_position + 1:]
            scrambled_before_apostrophe = word_scrambler(before_apostrophe)
            scrambled_word = f"{scrambled_before_apostrophe}'{after_apostrophe}"
        elif "'" in word and word[-1] in punctuation: # apostrophes with punctuation
            apostrophe_position = word.find("'")
            before_apostrophe = word[:apostrophe_position]
            after_apostrophe = word[apostrophe_position + 1:]
            scrambled_before_apostrophe = word_scrambler(before_apostrophe)
            scrambled_word = f"{scrambled_before_apostrophe}'{after_apostrophe}"
        else: # punctuation in a word
            parts = []
            current_part = ''
            for char in word:
                if char in punctuation:
                    if current_part:
                        parts += [current_part]
                    current_part = char
                else:
                    current_part += char
            if current_part:
                parts += [current_part]

            scrambled_parts = [word_scrambler(part) if part not in punctuation else part for part in parts]
            scrambled_word = ''.join(scrambled_parts)

        scrambled_words += [scrambled_word]
        scrambled_words_set += [word]

    final_message = ' '.join(scrambled_words)
    return final_message

original_message = "name@email.com. Y'all, In the kaleidoscope of existence, as the relentless metronome of time marches forward!!! Each day unveils an opulent tapestry of opportunities, like a symphony of serendipity conducted by destiny's maestro!!! Embrace the crescendo of life's complexities, for at the intersection of 11:59PM on December 31st, miracles are born anew, and the universe whispers its secrets to those who dare to listen."
scrambled_message = final_message(original_message)
print("Original Message:", original_message)
print("Scrambled Message:", scrambled_message)

# --------------------------------------------- original solution below
import random


def word_count_limits(word):
    if len(word) == 1: # for single-lettered words (mainly for 'a' and 'i', but just in case for 'y' or other letters as well), randomly replace with a vowel that is not itself
        if word.lower == 'a':
            vowels = ['e', 'i', 'o', 'u']
            set_random = random.randint(0, len(vowels) - 1)
            random_vowel = vowels[set_random]
            if word == 'A':
                return random_vowel.upper()
            else:
                return random_vowel
        elif word.lower == 'i':
            vowels = ['a', 'e', 'o', 'u']
            set_random = random.randint(0, len(vowels) - 1)
            random_vowel = vowels[set_random]
            if word == 'I':
                return random_vowel.upper()
            else:
                return random_vowel
        else:
            vowels = ['a', 'e', 'i', 'o', 'u']
            set_random = random.randint(0, len(vowels) - 1)
            random_vowel = vowels[set_random]
            if word != word.lower:
                return random_vowel.upper()
            else:
                return random_vowel

    elif len(word) == 2: # for two and three letter words, write them backwards
        scrambled_word = ""
        for i in word:
            scrambled_word = i + scrambled_word
        return scrambled_word
    else:
        scrambled_word = ""
        for i in word:
            scrambled_word = i + scrambled_word
        return scrambled_word


def even_odd_words(word):
    if len(word) % 2 == 0 and len(word) > 3: # for even lettered words: except for the first and last letter, shift every letter over one
        even = word[1:-1]
        rotated_even = even[-1] + even[:-1]
        scrambled_word = word[0] + rotated_even + word[-1]
        return scrambled_word

    elif len(word) % 2 == 1 and len(word) > 3: # odd letter words: shuffle all but the first and last letters
        first_letter = word[0]
        last_letter = word[-1]
        middle_letters = list(word[1:-1])
        for i in range(len(middle_letters) - 1, 0, -1):
            j = random.randint(0, i)
            middle_letters[i], middle_letters[j] = middle_letters[j], middle_letters[i]
        scrambled_word = first_letter + ''.join(middle_letters) + last_letter
        return scrambled_word


def word_scrambler(word):
    if len(word) > 3:
        return even_odd_words(word)
    else:
        return word_count_limits(word)



def final_message(message):
    words = message.split()
    scrambled_words = []
    scrambled_words_set = []
    punctuation = {',', '.', '?', '!', "'", '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', ';', '<', '>', '/', '|', '[', ']', '{', '}', '+', '=', '`', '~'}
    apostrophe = {"'s", "'t", "'d", "'m", "'re", "'ve", "'ll", "'all", "'t"}

    for word in words:
        if ':' in word: # deals with cases with time
            colon_position = word.find(":")
            before_colon = word[:colon_position]
            after_colon = word[colon_position + 1:]
            scrambled_before_colon = word_scrambler(before_colon)
            scrambled_after_colon = word_scrambler(after_colon)
            scrambled_word = f'{scrambled_before_colon}:{scrambled_after_colon}'
        elif "'" in word and word in apostrophe: # deals with apostrophes so that everyting after the apostrophe does not mix
            apostrophe_position = word.find("'")
            before_apostrophe = word[:apostrophe_position]
            after_apostrophe = word[apostrophe_position + 1:]
            scrambled_before_apostrophe = word_scrambler(before_apostrophe)
            scrambled_word = f"{scrambled_before_apostrophe}'{after_apostrophe}"
        elif "'" in word: # deals with apostrophes not stated
            apostrophe_position = word.find("'")
            before_apostrophe = word[:apostrophe_position]
            after_apostrophe = word[apostrophe_position + 1:]
            scrambled_before_apostrophe = word_scrambler(before_apostrophe)
            scrambled_word = f"{scrambled_before_apostrophe}'{after_apostrophe}"
        elif "'" in word and word[-1] in punctuation: # apostrophes with punctuation
            apostrophe_position = word.find("'")
            before_apostrophe = word[:apostrophe_position]
            after_apostrophe = word[apostrophe_position + 1:]
            scrambled_before_apostrophe = word_scrambler(before_apostrophe)
            scrambled_word = f"{scrambled_before_apostrophe}'{after_apostrophe}"
        else: # punctuation in a word
            parts = []
            current_part = ''
            for char in word:
                if char in punctuation:
                    if current_part:
                        parts += [current_part]
                    current_part = char
                else:
                    current_part += char
            if current_part:
                parts += [current_part]

            scrambled_parts = [word_scrambler(part) if part not in punctuation else part for part in parts]
            scrambled_word = ''.join(scrambled_parts)

        scrambled_words += [scrambled_word]
        scrambled_words_set += [word]

    final_message = ' '.join(scrambled_words)
    return final_message

original_message = "name@email.com. Y'all, In the kaleidoscope of existence, as the relentless metronome of time marches forward!!! Each day unveils an opulent tapestry of opportunities, like a symphony of serendipity conducted by destiny's maestro!!! Embrace the crescendo of life's complexities, for at the intersection of 11:59PM on December 31st, miracles are born anew, and the universe whispers its secrets to those who dare to listen."
scrambled_message = final_message(original_message)
print("Original Message:", original_message)
print("Scrambled Message:", scrambled_message)