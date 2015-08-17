#recursive

def fib1(n):
	if n<0:
		return 'Negative value!'
	elif n==0 or n==1:
		return n
	else:
		return fib1(n-1)+fib1(n-2)

#iterative
def fib2(n):
	x=0
	y=1
	i=2
	if n<0:
		return 'Negative value!'

	else:
		while i<=n:
			y,x=x+y,y
			i+=1
	return y
"""
def fib(n):
 if n==1 or n==2:
  return 1
 return fib(n-1)+fib(n-2)
print fib(5)
"""	
if __name__ == "__main__":
	x=raw_input("input your fib number:")
	print fib1(int(x))
	print fib2(int(x))
				