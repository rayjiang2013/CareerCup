'''
Created on Sep 23, 2015

@author: ljiang
'''
import pytest

from remov_duplicate_1_3 import remove_duplicate, remove_duplicate_2

@pytest.mark.parametrize("input, expected, func", [("123", '123', 1), ("1", '1', 1), ("222", '2', 1), ("abc123", 'abc123', 1),
                                                   ("abcba", 'abc', 1), ("abbc", 'abc', 1), ("aac", 'ac', 1), ("acc", 'ac', 1), ("", '', 1),
                                                   ("123", '123', 2), ("1", '1', 2), ("222", '2', 2), ("abc123", 'abc123', 2),
                                                   ("abcba", 'abc', 2), ("abbc", 'abc', 2), ("aac", 'ac', 2), ("acc", 'ac', 2), ("", '', 2),
                                                   ("123", '123', 3), ("1", '1', 3), ("222", '2', 3), ("abc123", 'abc123', 3),
                                                   ("abcba", 'abc', 3), ("abbc", 'abc', 3), ("aac", 'ac', 3), ("acc", 'ac', 3), ("", '', 3)])
def test_remove_duplicate(input, expected, func):
    if func ==1:
        assert remove_duplicate(input) == expected
    if func ==2:
        assert remove_duplicate_2(input) == expected