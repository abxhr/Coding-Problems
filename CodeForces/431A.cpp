/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int a[4];
    int total = 0;
    for (int i=0; i<4; i++){
        cin>>a[i];
    }
    string st;
    cin >> st;
    for(int i=0; i< st.length();i++){
        if (st[i] == '1'){
            total += a[0];
        }
        else if(st[i] == '2'){
            total += a[1];
        }
        else if(st[i] == '3'){
            total += a[2];
        }
        else{
            total += a[3];
        }
    }
    cout << total;
    return 0;
}