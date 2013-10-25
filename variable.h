#include<iostream>

using namespace std;

#define GET(a) ((a.t==1)?(a.v.d):\
		((a.t==2)?(a.v.ld):\
		((a.t==3)?(a.v.f):\
		((a.t==4)?(a.v.lf):\
		((a.t==5)?(a.v.c):\
		('\0')\
		)))))

union __var
{	int d;
	long ld;
	float f;
	double lf;
	char c;
};

class Var
{	public:
		union __var v;
		int t;

		void put(int a)
		{	v.d=a;
			t=1;
		}
		void put(long a)
		{	v.ld=a;
			t=2;
		}
		void put(float a)
		{	v.f=a;
			t=3;
		}
		void put(double a)
		{	v.lf=a;
			t=4;
		}
		void put(char a)
		{	v.c=a;
			t=5;
		}
};


