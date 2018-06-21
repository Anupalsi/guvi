#include <iostream>
#include <vector>
using namespace std;
class stack
{
public:
    int i;
    vector<int> mystack;
    vector <int> :: iterator itr;
   void push();
    void pop(){
         if (!mystack.empty()) {
            itr=--mystack.end();
             cout<<*itr<<endl;
            mystack.erase(itr);}
}
void display(){
    for(itr=mystack.end();itr>=mystack.begin();++itr)
    {itr=--mystack.end();
    cout<<*itr<<endl;
    
}}}};
void stack::push(){
        cout<<"enter the push number\n";
               
               int a;
               cin>>a;
               mystack.push_back(a);
   }
int main()
{ 
    int i;
    stack s;
      do{
    cout<<"1.push\n";
    cout<<"2.pop\n";
    cout<<"3.exit\n";
    cout<<"4.display\n";
    cin>>i;
    switch(i){
        case 1:s.push();
            break;
        case 2:s.pop();
           break;
          case 3:break;
          case 4:s.display();
          break;
    }}while(i!=3);
 return 0;       
}
