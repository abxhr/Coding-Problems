/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

//a = 97
//total = 26
//half = 13

#include <bits/stdc++.h>

using namespace std;

int main()
{
    string in;
    int count = 0;
    cin >> in;
    int flag, diff;
    flag = 97;
    for(int i=0;i<in.length();i++){
        diff = abs(flag - in[i]);
        if(diff > 13){
            diff = 26 - diff;
        }
        count += diff;
        flag = in[i];
    }
    cout << count;
    return 0;
}