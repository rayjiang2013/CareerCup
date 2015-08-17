#Example: Given two numbers m and n, write a method to return the first number r that is
#divisible by both (e.g., the least common multiple).

def find_prime(number):
	list=[]
	if number >= 2:
		list.append(2)
	if number >=3:
		list.append(3)
	for i in xrange(3,number+1): 
		for j in xrange(2,(i+1)/2):
			if i%j==0:
				break
			elif j<(i-1)/2: 
				continue
			else: list.append(i)
	return list

def factory_prime(number,fact_list):
	lst=find_prime(number)		
	for i in lst:
		if number%i==0:
			fact_list.append(i)
			number=number/i
			if number !=1:
				factory_prime(number,fact_list)
			break
	return fact_list

def least_common_multiple(m,n):
	list_1=factory_prime(m,[])
	print list_1
	list_2=factory_prime(n,[])
	print list_2
	list_3=[]
	list_5=list(list_2)
	z=1
	for x in list_1:
		if x in list_5:
			list_3.append(x)
			list_5.remove(x)
				
	print list_1
	print list_2
	list_4=list_1+list_2
	print list_4
	for h in list_3:
		if h in list_4:
			list_4.remove(h)
	for j in list_4:
		z=z*j
	print z

def least_common_multiple_2(m,n):
	large=int(m)
	if m<n:
		large=int(n)
	while True:
		if large%m==0 and large%n==0:
			return large
		large=large+1

def greatest_common_divisor(m,n):
	large=m
	small=n
	if m<n:
		large=n
		small=m
	while small:
		large,small=small,large%small
	return large
		
def least_common_multiple_3(m,n):
	print greatest_common_divisor(m,n)
	return m*n/greatest_common_divisor(m,n)
	
		
	
if __name__=="__main__":	
	#print find_prime(12)
	#print factory_prime(12,[])
	#least_common_multiple(1,2)
	print least_common_multiple_2(4,5)
	print least_common_multiple_3(4,5)