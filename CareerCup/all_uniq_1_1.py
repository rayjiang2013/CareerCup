'''
Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?
'''
def uniq_or_not(str):
    if str == '':
        return True
    lst = []
    for i in str:
        if i not in lst:
            lst.append(i)
        else:
            return False
    return True

def uniq_or_not_2(str):
    if str == '':
        return True
    lst = 256 * [None]
    for i in str:
        int_i = ord(i)
        if lst[int_i] == True:
            return False
        lst[int_i] = True
    return True
