'''
Created on Sep 22, 2015

@author: ljiang
'''
import pytest

from all_uniq_1_1 import *

@pytest.mark.parametrize("input, output, func", [('abcabc', False, 1), ('a', True, 1), ('123', True, 1), ('', True, 1), ('a186  ', False, 1),
                                                 ('abcabc', False, 2), ('a', True, 2), ('123', True, 2), ('', True, 2), ('a186  ', False, 2)])
def test_all_uniq(input, output, func):
    if func == 1:
        assert uniq_or_not(input) == output
    if func == 2:
        assert uniq_or_not_2(input) == output
