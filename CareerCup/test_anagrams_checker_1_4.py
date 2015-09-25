'''
Created on Sep 23, 2015

@author: ljiang
'''
import pytest
from anagrams_checker_1_4 import check_anagram, check_anagram_2, check_anagram_3

@pytest.mark.parametrize("st1, st2, expected, func", [('abc', 'bca', True, 1), ('abc', 'bc', False, 1), ('abbc', 'bbca', True, 1),
                                                      ('123 abc', 'c12b a3', True, 1), (' ', ' ', True, 1), ('', ' ', False, 1),
                                                      ('123', '123 ', False, 1), ('ab/*1', '1*/ba', True, 1), ('ccc', 'c', False, 1),
                                                      ('abc', 'bca', True, 2), ('abc', 'bc', False, 2), ('abbc', 'bbca', True, 2),
                                                      ('123 abc', 'c12b a3', True, 2), (' ', ' ', True, 2), ('', ' ', False, 2),
                                                      ('123', '123 ', False, 2), ('ab/*1', '1*/ba', True, 2), ('ccc', 'c', False, 2),
                                                      ('abc', 'bca', True, 3), ('abc', 'bc', False, 3), ('abbc', 'bbca', True, 3),
                                                      ('123 abc', 'c12b a3', True, 3), (' ', ' ', True, 3), ('', ' ', False, 3),
                                                      ('123', '123 ', False, 3), ('ab/*1', '1*/ba', True, 3), ('ccc', 'c', False, 3)])
def test_anagrams_checker(st1, st2, func, expected):
    if func == 1:
        assert check_anagram(st1, st2) == expected
    if func == 2:
        assert check_anagram_2(st1, st2) == expected
    if func == 3:
        assert check_anagram_3(st1, st2) == expected