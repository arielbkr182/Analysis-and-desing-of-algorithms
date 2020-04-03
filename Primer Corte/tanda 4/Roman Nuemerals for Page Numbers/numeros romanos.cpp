#include<bits/stdc++.h>
using namespace std;

int func(int);
int main()
{
    int n;
    cin>>n;
    func(n);
    cout<<endl;
    return 0;
}
int func(int n)
{
    int arr[14]={1000,900,500,400,100,90,60,50,40,10,9,5,4,1};
    for(int i=0;i<14;i++){
        while(n>=arr[i]){
            n = n-arr[i];
            if(arr[i] == 1000) cout<<"M";
            else if(arr[i] == 900) cout<<"CM";
            else if(arr[i] == 500) cout<<"D";
            else if(arr[i] == 400) cout<<"CD";
            else if(arr[i] == 100) cout<<"C";
            else if(arr[i] == 90) cout<<"XC";
            else if(arr[i] == 60) cout<<"LX";
            else if(arr[i] == 50) cout<<"L";
            else if(arr[i] == 40) cout<<"XL";
            else if(arr[i] == 10) cout<<"X";
            else if(arr[i] == 9) cout<<"IX";
            else if(arr[i] == 5) cout<<"V";
            else if(arr[i] == 4) cout<<"IV";
            else if(arr[i] == 1) cout<<"I";
        }
    }
}
