/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    int a[n+1];
    bool is[n+1];
    for(int i=1;i<=n;i++){
        cin >> a[i];
    }
    for(int i=1;i<=n;i++){
        is[i] = false;
    }
    is[0] = false;
    int chk = n;
    for(int i=1;i<=n;i++){
        int x = a[i];
        is[x] = true;
        if(x==chk){
            while(is[chk]){
                cout << chk << " ";
                chk--;
            }
            cout << "\n";
        }
        else{
            cout << "\n";
        }
    }
    return 0;
}