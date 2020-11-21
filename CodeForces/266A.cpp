#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    string a;
    cin >> a;
    a += 'z';
    int count = 0;
    for (int i = 0; i < a.length() - 1; i++){
        if(a[i] == a[i+1]){
            count += 1;
        }
    }
    cout << count;
}