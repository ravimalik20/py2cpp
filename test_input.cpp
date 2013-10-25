#include<variable.h>
#include<raw_input.h>
#define and &&
#define or ||
int main()
{
Var a;
a.put(10);

Var b;
b.put(20);

Var c;
c.put((int)(raw_input("Hello World")));
if(GET(a)>GET(b))
{
cout<<"Hello World";
cout<<"bla nlandcndc";
}
else
{
cout<<"Gotcha!!";
cout<<"bla nlandcndc";
}
a.put(0);
b.put(GET(b)+fetch(GET(a)));
cout<<GET(b)<<GET(a);
while(GET(a)!=10)
{
cout<<GET(a);
	a.put(GET(a)+1);
cout<<GET(a);
cout<<GET(a)+20;
}
class hello_world
{

}

return 0;
}