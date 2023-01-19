from app import hello
from app import extract_sentiment
from app import text_contain_word
from app import bubble_sort
import pytest


def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want


testdata1 = ["I think today will be a great day"]


@pytest.mark.parametrize('sample', testdata1)
def test_extract_sentiment(sample):
    sentiment = extract_sentiment(sample)

    assert sentiment > 0


testdata2 = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
]


@pytest.mark.parametrize('sample, word, expected_output', testdata2)
def test_text_contain_word(sample, word, expected_output):
    assert text_contain_word(word, sample) == expected_output


testdata3 = [
    ([1, 3, 5, 2, 4, 6], [1, 2, 3, 4, 5, 6]),
    ([4, 3, 2, 1, 0], [0, 1, 2, 3, 4]),
    ([1, 7, 3, 6, 4], [1, 3, 4, 6, 7]),
    ([6, 3, 2, 6, 0, 0], [0, 0, 2, 3, 6, 6])
]

# Faza red
@pytest.mark.parametrize('sample, sorted_sample', testdata3)
def test_bubble_sort(sample, sorted_sample):
    assert bubble_sort(sample) == sorted_sample
