//Name: Xiaohan Sun
//Email: xiaohan.sun94@myhunter.cuny.edu
//Date: May 01, 2022
//This program prints the change in population of the the United States

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int y = 2017;
    double n, p;
    cout<<"Enter a number of year:";
    cin>>n;
    p = 325.7;
    cout<<setprecision(2)<<fixed;
    
    for (int i = 0; i < n; ++i)
    {
        cout<<"Year"<<y<<" "<<p<<endl;
        ++y;
        p*=1.004;
    }
    return 0;
}