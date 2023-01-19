from typing import List
from textblob import TextBlob


def hello(name):
    output = f'Hello {name}'
    return output


def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity


def text_contain_word(word: str, text: str):
    return word in text


# Faza Green i poźniejsza Faza Refactor
def bubble_sort(lst_original: List[int]) -> List[int]:
    lst = lst_original[:]
    n = len(lst)
    counter = 0
    change_position = 1
    while n > 1 and change_position > 0:
        change_position = 0
        for i in range(1, n):
            counter += 1
            if lst[i - 1] > lst[i]:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
                change_position += 1
        n -= 1
    return lst
