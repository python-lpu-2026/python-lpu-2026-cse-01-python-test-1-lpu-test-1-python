from question2 import second_highest

def test_q2_basic():          # 3 marks
    assert second_highest([10, 20, 30]) == 20

def test_q2_duplicates():     # 3 marks
    assert second_highest([5, 5, 5]) is None

def test_q2_negative():       # 2 marks
    assert second_highest([-1, -2, -3]) == -2

def test_q2_single():         # 1 mark
    assert second_highest([10]) is None

def test_q2_invalid():        # 1 mark
    assert second_highest("abc") is None
