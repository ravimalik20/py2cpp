#include"variable.h"
#include"raw_input.h"
#include<math.h>
int main()
{
Var a;
a.put( 10 );

Var b;
b.put( 20 );
if(GET(a) >  20  and GET(b) <  30 )
{
cout<< "  Hello World  " ;
}
else
{
cout<< "  Go to Hell!!  " ;
}

return 0;
}