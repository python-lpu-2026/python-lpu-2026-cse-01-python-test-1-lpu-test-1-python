from question1 import count_vowels

def test_q1_basic():          # 3 marks
    assert count_vowels("hello") == 2

def test_q1_case():           # 2 marks
    assert count_vowels("AEIOU") == 5

def test_q1_symbols():        # 2 marks
    assert count_vowels("Hello World!") == 3

def test_q1_no_vowels():      # 2 marks
    assert count_vowels("bcdfg") == 0

def test_q1_invalid():        # 1 mark
    assert count_vowels(12345) == 0
