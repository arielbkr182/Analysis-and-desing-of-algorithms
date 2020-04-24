#include <iostream>
using namespace std;
int main(){
    int i,fact=1,num;
         cout<<"Ingresa un numero"<<endl;
        cin>>num;
        for(i=1;i<num+1;i++){
            fact=fact*i;
        }
         cout<<fact;
      return 0;
}

