/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    int a[n];
    for(int i=1;i<=n;i++){
        cin >> a[i];
    }
    int m;
    cin >> m;
    int x,y;
    for(int i=1;i<=m;i++){
        cin >> x >> y;
        a[x-1]+=y-1;
        a[x+1]+=a[x]-y;
        a[x]=0;
    }
    for(int i=1;i<=n;i++){
        cout<< a[i] <<"\n";
    }
    return 0;
}