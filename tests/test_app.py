from app import add,sub

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(1, 1) == 2
    assert sub(50,10) == 40
    assert add(10,15) == 25