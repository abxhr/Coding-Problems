/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while(t--){
        long long l,r;
        cin >> l >> r;
        long long diff = r-l;
        int val = 1;
        while(diff--){
           val += 2;
        }
        cout << val << "\n";
    }
    return 0;
}