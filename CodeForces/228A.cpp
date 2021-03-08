/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int s[4];
    for(int i=0;i<4;i++){
        cin >> s[i];
    }
    int c = 0;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(i!=j){
                if((s[i] > 0) && (s[i] == s[j])){
                    c++;
                    s[j] = 0;
                }
            }
        }
    }
    cout << c;
    return 0;
}