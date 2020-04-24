#include <iostream>

using namespace std;

int fibonacci(int n);

int main(int argc, char *argv[]) {
 int n;
 cout<<"ingrese numero"<<endl;
 cin>>n;
 
 cout<<"el resultado es:"<<fibonacci(n)<<endl;
 return 0;
}


int fibonacci(int a){
 if((a==1 || a==2)){
  return 1;
 }
 else{
  return(fibonacci(a-1)+fibonacci(a-2));
 }
 
}
