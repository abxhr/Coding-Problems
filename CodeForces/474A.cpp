/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    string k1 = "qwertyuiop[]";
    string k2 = "asdfghjkl;'";
    string k3 = "zxcvbnm,./";
    char shift;
    cin >> shift;
    string s;
    cin >> s;
    for(int i=0;i<s.size();i++){
        for(int a=0;a<k1.size();a++){
            if(s[i] == k1[a]){
                if(shift == 'R'){
                    cout << k1[a-1];
                }
                else{
                    cout << k1[a+1];
                }
                break;
            }
        }
        for(int a=0;a<k2.size();a++){
            if(s[i] == k2[a]){
                if(shift == 'R'){
                    cout << k2[a-1];
                }
                else{
                    cout << k2[a+1];
                }
                break;
            }
        }
        for(int a=0;a<k3.size();a++){
            if(s[i] == k3[a]){
                if(shift == 'R'){
                    cout << k3[a-1];
                }
                else{
                    cout << k3[a+1];
                }
                break;
            }
        }
    }
    return 0;
}