#!/usr/bin/python3
"""Type-annotated function sum_mixed_list that takes a list mxd_lst of floats and integers and returns their sum as a float."""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of the list of floats and integers."""
    return sum(mxd_lst)