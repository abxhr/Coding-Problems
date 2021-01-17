/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    int s = 97;
    char c[k];
    for(int i = 0;i<k;i++){
        c[i] = s++;
    }
    int s2 = 0;
    for(int i = 0;i<n;i++){
        cout << c[s2++];
        if(s2 >= k) s2 = 0; 
    }
}