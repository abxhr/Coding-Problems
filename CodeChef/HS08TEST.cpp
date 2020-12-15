#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() 
{
        int wit; 
        cin>> wit;
        float balance;
        cin>>balance;
        if(wit%5==0 && (wit+0.5) <= balance)
        {
            balance-=(wit+0.5);
        }
        
        cout<<fixed<<setprecision(2)<<balance<<endl;
	return 0;
}