from basic_operations import add
from advanced_operations import sine

def test_combined_operations():
    result = add(5,5) + sine(0)
    assert result == 10
