/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, t, k, d;
    cin >> n >> t >> k >> d;
    
    if(d < t*((ceil(n*1.0/k)) - 1)){
        cout << "YES";
    }
    else{
        cout << "NO";
    }

    return 0;
}