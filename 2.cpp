#include"variable.h"
#include"raw_input.h"
int main()
{
Var n;
n.put((int)(raw_input("Enter the number to check if prime:")));

Var a;
a.put(2);

Var b;
b.put(1);
while(GET(a)*GET(a)<GET(n))
{
if(GET(n)%GET(a)==0)
{
cout<<"Not Prime";
b.put(0);
break;
}
}
if(GET(b)==1)
{
cout<<"Prime";
}

return 0;
}