from typing import List, Dict, Tuple

def index_multiplication(test_tup1: Tuple[Tuple[int]], test_tup2: Tuple[Tuple[int]]) -> Tuple[Tuple[int]]:
    """
	Write a function to perform index wise multiplication of tuple elements in the given two tuples.
	"""
    ### Canonical solution below ###
    pass

### Unit tests below ###
def check(candidate):
    assert candidate(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 21), (12, 45), (2, 9), (7, 30))
    assert candidate(((2, 4), (5, 6), (3, 10), (2, 11)), ((7, 8), (4, 10), (2, 2), (8, 4))) == ((14, 32), (20, 60), (6, 20), (16, 44))
    assert candidate(((3, 5), (6, 7), (4, 11), (3, 12)), ((8, 9), (5, 11), (3, 3), (9, 5))) == ((24, 45), (30, 77), (12, 33), (27, 60))

def test_check():
    check(index_multiplication)

