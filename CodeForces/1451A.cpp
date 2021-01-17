/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        int m = 0;
        if (n <= 3) m = n - 1;
        else{
            if(n%2 == 0) m = 2;
            else m = 3;
        } 
    cout << m << "\n";
    }
}