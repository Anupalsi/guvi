#include <iostream>
#include <vector>
using namespace std;
 
int main()
{
    int i;
    vector<int> mystack;
    vector <int> :: iterator itr;
   do{
    cout<<"1.push\n";
    cout<<"2.pop\n";
    cout<<"3.exit\n";
    cin>>i;
    switch(i){
        case 1:cout<<"enter the push number\n";
               
               int a;
               cin>>a;
               mystack.push_back(a);
               break;
    
        case 2: if (!mystack.empty()) {
            itr=--mystack.end();
            mystack.erase(itr);}
        break;
        case 3:break;
        
        default:cout<<"invalid";
        break;
    }
   }while(i!=3);
    
while( mystack.size()!=0)
{
    itr=--mystack.end();
    cout<<*itr<<endl;
    mystack.erase(itr);
}
return 0;
    
    }
