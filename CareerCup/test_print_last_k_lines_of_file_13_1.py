'''
Created on Jul 28, 2015

@author: ljiang
'''
import pytest
from print_last_k_lines_of_file_13_1 import print_last_k_lines_of_file

def test_print_last_k_lines_of_file():  
    with open("example.txt","r") as f:
        print_last_k_lines_of_file(f,5)
