#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    int mx = 0;
    int mn = 1000000005;
    int c1 = 0;
    int c2 = 0;
    cin >> n;
    int a[n];
    for(int i=1;i<=n;i++){
        cin >> a[i];
        mx = max(mx,a[i]);
        mn = min(mn,a[i]);
    }
    for(int i=1;i<=n;i++){
        if(a[i]==mn) c1++;
        if(a[i]==mx) c2++;
    }
    if(mn==mx) cout << "0";
    else cout << (n-c1-c2); 
    return 0;
}