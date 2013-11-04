n=int(raw_input("Enter the number to check if prime:"))

a=2

b=1

while a*a<=n:
	if n%a==0:
		print "Not Prime"

		b=0

		break
	a=a+1

if b==1:
	print "Prime"
