//Name: Xiaohan Sun
//Email: xiaohan.sun94@myhunter.cuny.edu
//Date: May 01, 2022
//This program asks the user for the year born, and continue asking until the number entered that is 2018 or earlier

#include <iostream>
using namespace std;

int main()
{
    int y;
    cout<<"Enter a born year:";
    cin>>y;
    
    while(y>2018)
    {
        cout<<"Enter a future year"<<endl;
        cout<<"Enter a born year:";
        cin>>y;
    }
    
    cout<<"You entered:"<<y<<endl;
    return 0;
}