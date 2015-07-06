n=10

if n<0:
	print "Cannot generate factorial of negative numbers."

else:
	a=1
	while n>0:
		a=a*n
		n=n-1

	print a
