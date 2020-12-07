#include <bits/stdc++.h>

using namespace std;

int main() {
    int n,b,d;
    cin >> n >> b >> d;
    int a[n];
    for(int i=0;i<n;i++){
        cin >> a[i];
    }
    int w = 0;
    int c = 0;
    for(int i=0;i<n;i++){
        if(a[i] <= b){
            w += a[i];
        }
        if(w > d){
            w = 0;
            c++;
        }
    }
    cout << c;
    return 0;
}