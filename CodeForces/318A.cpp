/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    long long k, val;
    long double n;
    cin >> n >> k;
    long long c = ceil(n/2);
    if(k <= c){
        val = 2*k - 1;
    }
    else{
        val = 2*(k - c);
    } 
    cout << val;
    return 0;
}