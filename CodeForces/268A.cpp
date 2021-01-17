/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    int a[n],b[n];
    for(int i=0;i<n;i++){
        cin >> a[i] >> b[i];
    }
    int count = 0;
    for(int i = 0;i<n;i++){
        for(int j =0; j<n;j++){
            if(i!=j){
                if(a[i] == b[j]) count++;
            }
        }
    }
    cout << count;
    return 0;
}