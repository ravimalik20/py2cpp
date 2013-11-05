#include"variable.h"
#include"raw_input.h"
#include<math.h>
int main()
{
Var a;
a.put( 10 );

Var b;
b.put( 20 );
if(GET(a) <  20  && GET(b) >  30  || GET(b) -  20  <  30  && GET(a) !=  4 )
{
cout<< "  Hello World  " ;
}
else
{
cout<< "  Go to Hell!!  " ;
}

return 0;
}