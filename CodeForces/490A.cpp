/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    int t[n],a1[5000],a2[5000],a3[5000];
    int a1c=0,a2c=0,a3c=0;
    for (int i=0;i<n;i++){
        cin >> t[i];
    }
    for(int i =0;i<n;i++){
        if(t[i] == 1) a1[a1c++] = i+1;
        else if(t[i] == 2) a2[a2c++] = i+1;
        else a3[a3c++] = i+1;
    }
    int k = min(a1c,a2c);
    k = min(k,a3c);
    cout << k << "\n";
    for(int i=0,j=0,p=0;i<a1c,j<a2c,p<a3c,k>0;i++,j++,p++,k--){
        cout << a1[i] << " " << a2[j] << " " << a3[p] << "\n";
    }
}