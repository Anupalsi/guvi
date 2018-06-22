#include <iostream>
#include <vector>
using namespace std;
class reversal
{
	vector <char> s;
   
    public:
    vector <char> :: iterator itr;
    void push(char);
    
    char pop();
    
    
    };
void reversal::push(char val)    
{
	s.push_back(val);
}

char reversal::pop()
{ char m;
//vector <char> :: iterator itr;
	itr=--s.end();
    m=*itr;
    //cout<<m;
    s.erase(itr);
    return m;
    
}
int main()
{int i;
	char b[100],c[100];
	reversal re;
	cout<<"enter the string\n";
	cin.get(b,100);
	for(i=0;b[i]!='\0';i++)
	{
		re.push(b[i]);
}
for(i=0;b[i]!='\0';i++)
{

		c[i]=re.pop();
	
}
cout<<c;
return 0;
}
