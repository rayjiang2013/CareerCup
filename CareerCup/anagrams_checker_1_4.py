'''
Created on Sep 23, 2015

@author: ljiang
'''
from __builtin__ import True
def check_anagram(st1, st2):
    st1, st2 = list(st1), list(st2)
    if len(st1) != len(st2):
        return False
    x=0
    while x < len(st1):
        if st1[x] in st2:
            del st2[st2.index(st1[x])]
            del st1[x]
        else:
            return False
    return True

def check_anagram_2(st1, st2):
    st1, st2 = list(st1), list(st2)
    st1.sort()
    st2.sort()
    if st1 == st2:
        return True
    else:
        return False

#insertion sort
def check_anagram_3(st1, st2):
    st1, st2 = list(st1), list(st2)
    temp = []
    y = 1
    for x in st1:
        if len(temp) == 0:
            temp.append(x)
            continue
        while y < len(temp):
            if x < temp[y]:
                temp.insert(y, x)
            elif y == len(temp)-1:
                temp.append(x)
            y+=1
    st1 = temp
    temp = []
    y = 1
    for x in st2:
        if len(temp) == 0:
            temp.append(x)
            continue
        while y < len(temp):
            if x < temp[y]:
                temp.insert(y, x)
            elif y == len(temp)-1:
                temp.append(x)
            y+=1
    st2 = temp    
    if st1 == st2:
        return True
    else:
        return False