from typing import List, Dict, Tuple

def tuple_to_dict(test_tup: Tuple[int]) -> Dict[int, int]:
    """
	Write a function to convert the given tuple to a key-value dictionary using adjacent elements. https://www.geeksforgeeks.org/python-convert-tuple-to-adjacent-pair-dictionary/
	"""
    ### Canonical solution below ###
    pass

### Unit tests below ###
def check(candidate):
    assert candidate((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
    assert candidate((1, 2, 3, 4, 5, 6)) == {1: 2, 3: 4, 5: 6}
    assert candidate((7, 8, 9, 10, 11, 12)) == {7: 8, 9: 10, 11: 12}

def test_check():
    check(tuple_to_dict)

