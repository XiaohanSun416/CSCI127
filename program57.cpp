//Name: Xiaohan Sun
//Email: xiaohan.sun94@myhunter.cuny.edu
//Date: May 01, 2022
//This program asks the user for the month of the year (as a number), and prints

#include <iostream>
using namespace std;

int main()
{
    int m;
    cout<<"Enter a number:";
    cin>>m;
    
    if(m<=3 || m>11)
    {
        cout<<"Happy Winter"<<endl;
    }
    else if(m>3 and m<7)
    {
        cout<<"Happy Spring"<<endl;
    }
    else if(m>=7 and m<9)
    {
        cout<<"Happy Summer"<<endl;
    }
    else
    {
        cout<<"Happy Fall"<<endl;
    }
    return 0;
}