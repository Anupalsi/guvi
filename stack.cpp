#include <iostream>
#include <stack>
using namespace std;
 
int main()
{
    int i;
    stack<int> mystack;
   do{
    cout<<"1.push\n";
    cout<<"2.pop\n";
    cout<<"3.exit\n";
    cin>>i;
    switch(i){
        case 1:cout<<"enter the push number\n";
               
               int a;
               cin>>a;
               mystack.push(a);
               break;
    
        case 2: if (!mystack.empty()) {
            
            mystack.pop();}
        break;
        case 3:break;
        
        default:cout<<"invalid";
        break;
    }
   }while(i!=3);
    
while( mystack.size()!=0)
{
    cout<<mystack.top()<<" ";
    mystack.pop();
}
return 0;
    
    }
