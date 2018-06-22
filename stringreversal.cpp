# your code goes here
#include <iostream>
#include <vector>
using namespace std;
class reversal:{
	vector<char> s;
    vector <char> :: iterator itr;
    public
    void push(char);
    int empty();
    char pop();
    
    
    };
void reversal:push(char val)    
{
	s.push_back(val);
}
int empty()
{
	if(s.empty())
	return 0
	else
	return 1
}
char pop()
{
	itr=--s.end();
    m=*itr;
    s.erase(itr);
    return m;
    
}
int main()
{
	char b[100],c[100];
	reversal re;
	cout<<"enter the string\n";
	cin.get(b,100);
	for(i=0;i!='\o';i++)
	{
		re.push(b[i]);
}
for(i=0;i!='\o';i++)
{
	a=re.empty();
	if(a==1)
		c[i]=re.pop();
	
}
cout<<c
return 0;
}
