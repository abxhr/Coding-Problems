/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    int a[n];
    int h = 0;
    int count = 0;
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    for(int i = 0; i < n; i++){
        if(a[i] > 0) h += a[i];
        else{
            if(h){
                h -= 1;
            }
            else count += 1;
        }
    }
    cout << count;
}