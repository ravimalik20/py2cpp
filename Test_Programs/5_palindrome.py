num=int(raw_input("Enter the number to check if palindrome:"))

t=num

temp=0
digit=-1
a=1

l=0

# Finding length of the number:
while t>0:
	t=t/10
	l=l+1
	a=a*10

a=a/10

t=num

while t>0:
	digit=t%10
	t=t/10
	temp=temp+digit*a;
	a=a/10	

if (num-temp)==0:
	print "Number is palindrome!!"
else:
	print "Number not palindrome!!"
