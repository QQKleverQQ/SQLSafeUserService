from app.security import simple_hash

def test_simple_hash_repeat():
    assert simple_hash("abc") == simple_hash("abc")


def test_simple_hash_diff():
    assert simple_hash("abc") != simple_hash("abcd")
