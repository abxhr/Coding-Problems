#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    int count = 0;
    int prev = 00;
    for(int i = 0; i < n; i++){
        int cur;
        cin >> cur;
        if (!(cur == prev)){
            count += 1;
        }
        prev = cur;
    }
    cout << count;
    }
    