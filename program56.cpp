//Name: Xiaohan Sun
//Email: xiaohan.sun94@myhunter.cuny.edu
//Date: May 01, 2022
//This program asks the user for a number and draws a triangle of that height and width using 'character graphics'

#include <iostream>
using namespace std;

int main()
{
    int r;
    cout<<"Enter a number:";
    cin>>r;
    
    for(int i = 0; i < r; i++)
    {
        for(int j = 0; j <= i; j++)
        {
                cout<<"*";
        }
        cout<<endl;
    }
    return 0;
}