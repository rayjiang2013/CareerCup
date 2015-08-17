'''
The objective is to find maximum forward difference between two numbers in a series of numbers. The program should print out the max difference and the index location of the two elements used to calculate the said difference in following format

diff:<max(a[j] - a[i])>::loc(i,j)   where j > i

e.g.#1

arr = [10 5 1 3] should print

diff:2::loc(2,3)

Here are the list of allowed differences

a[i]    a[j]    a[j]-a[i]
10      5       -5
10      1       -9
10      3       -7
5       1       -4
5       3       -2
1       3       2(max)
'''
def max_diff(arr):
    max=arr[1]-arr[0]
    location=[]
    for i in xrange(0,len(arr)):
        for j in xrange(i+1,len(arr)):
            if arr[j]-arr[i]>max:
                max=arr[j]-arr[i]
                location=[i,j]
    print "diff:"+str(max)+"::loc("+str(location[0])+","+str(location[1])+")"
    
def max_diff_2(arr):
    diff=arr[1]-arr[0]
    min=arr[0]
    location=[]
    for i in arr[1:]:
        if diff<i-min:
            diff=i-min
        if i<min:
            min=i
        location=[arr.index(min),arr.index(i)]
    print "diff:"+str(diff)+"::loc("+str(location[0])+","+str(location[1])+")"
            

arry=[10,5,1,3] 
max_diff(arry)
max_diff_2(arry)
    