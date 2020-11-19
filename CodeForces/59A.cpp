#include <bits/stdc++.h>

using namespace std;

int main() {
    string a;
    cin >> a;
    int u = 0;
    int l = 0;
    for(int i = 0; i < a.length(); i++){
        if (a[i] >= 97 && a[i] <= 122){
            l += 1;
        }
        else{
            u += 1;
        }
        }
    for(int i =0; i < a.length(); i++){
        if(u > l){
            a[i] = toupper(a[i]);
            cout << a[i];
        }
        else{
            a[i] = tolower(a[i]);
            cout << a[i];
        }
    }
    }
    