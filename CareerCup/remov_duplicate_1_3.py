'''
Created on Sep 22, 2015

@author: ljiang

Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer. NOTE: One or two additional variables are fine. An extra copy of the array is not.
FOLLOW UP
Write the test cases for this method.

'''
#Cannot do it in python as in python string is immutable

#extra space needed for slicing, n^2 complexity
def remove_duplicate(st):
    st = list(st)
    j=1
    i=1
    while i < len(st):
        if st[i] in st[:j]:
            del st[i]
        else:
            i+=1
            j+=1
    return ''.join(st)

# extra space for a list with non-duplicate elements, n^2 complexity
def remove_duplicate_2(st):
    uniq_list=[]
    for x in st:
        if x in uniq_list:
            continue
        else:
            uniq_list.append(x)
    return ''.join(uniq_list)


# n complexity
def remove_duplicate_3(st):
    ascii_list = 256 * [None]
    st = list(st)
    x = 0
    while x < len(st):
        if ascii_list[ord(x)] == True:
            del st[x]
            continue
        else:
            ascii_list[ord(x)] = True
            x+=1
    return st

if __name__ == '__main__':
    print remove_duplicate("stts")
    print remove_duplicate_2('stts')