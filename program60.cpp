//Name: Xiaohan Sun
//Email: xiaohan.sun94@myhunter.cuny.edu
//Date: May 01, 2022
//This program asks the user for a whole number between -31 and 31 and prints out the number in "two's complement" notation, using the following algorithm

#include <iostream>
using namespace std;

int main()
{
    int n,x,b;
    cout<<"Enter a number: ";
    cin>>n;
    
    if(n<0)
    {
        cout<<1;
        x=32+n;
    }
    else if(n>=0)
    {
        cout<<0;
        x=n;
    }
    
    b=16;
    while(b>0.5)
    {
        if(x>=b)
        {
            cout<<1;
        }
        else
        {
        cout<<0;
        }
        x=x%b;
        b=b/2;
    }
    cout<<"\n";
}