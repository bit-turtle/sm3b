#include <stdio.h>
#define C(c,r) case c:r;break;
#define S(a,b) {int c=a;a=b;b=c;f=1;}
#define I "%i,\n"
int main(int n,char**p){for(int m[64]={0},x=0,y=0,a=0,v=0,f=1,j=0,i=0;p[1][i];j?i:i++,printf("SM3B:X%i,Y%i,A%i,V%i,F%i,J%i,I%i,M[%i]%i\n",x,y,a,v,f,j,i,a,m[a]),j=0)switch(p[1][i]){C('0',x=f?--f:x<<1)C('1',x=f?f--|1:x<<1|1)C('+',x=(f=1,v+=x))C('-',x=(f=1,v-=x))C('#',S(x,y))C('@',S(x,a))C('$',S(x,m[a]))C('?',if(x&&++j)S(a,i)f=1)}}
