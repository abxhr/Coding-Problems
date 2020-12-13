#include<bits/stdc++.h>

using namespace std;

int main(){
    long long s,n;
    while(cin >> n && n!=0){
        s = (int)sqrt(n);
        if(s*s == n) cout << "yes\n";
        else cout << "no\n";
    }
    return 0;
}