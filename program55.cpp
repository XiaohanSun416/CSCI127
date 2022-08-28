//Name: Xiaohan Sun
//Email: xiaohan.sun94@myhunter.cuny.edu
//Date: May 01, 2022
//This program converts kilometers to miles

#include <iostream>
#include <math.h>

int main()
{
    float kilometers;
    std::cout<<"Enter kilometers:";
    std::cin>>kilometers;
    float miles = 0.621371*kilometers;
    std::cout<<miles<<"Miles";
}