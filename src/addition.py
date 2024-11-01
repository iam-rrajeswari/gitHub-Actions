# app.py
# This is a test add commit
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 2
    assert add(1, -1) == 0
