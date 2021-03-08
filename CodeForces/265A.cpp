/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    string s,c;
    cin >> s;
    cin >> c;
    int pos = 1;
    int cur = 0;
    for(int i =0;i<c.length();i++){
        if(s[cur] == c[i]) {
            pos++;
            cur++;
        }
    }
    cout << pos;
    return 0;
}