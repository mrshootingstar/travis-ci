# content of test_sample.py
def inc(x):
    return x + 1


def test_answer_fail():
    assert inc(3) == 4



def test_answer_succeed():
    assert inc(13) == 14


