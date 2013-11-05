#include"variable.h"
#include"raw_input.h"
#include<math.h>
int main()
{
Var n;
n.put((int) ( raw_input (  "  Enter the number to calculate factorial  "  )  ) );
if(GET(n) <  0 )
{
cout<< "  Cannot generate factorial of negative numbers.  " ;
}
else
{

Var a;
a.put( 1 );
while(GET(n) >  0 )
{
a.put(GET(a) * GET(n));
n.put(GET(n) -  1 );
}
cout<<GET(a);
}

return 0;
}