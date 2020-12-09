#include <bits/stdc++.h>

using namespace std;

int main() {
    long long int n,x ;
    cin >> n >> x;
    char s;
    long long int d;
    long long int c = 0;
    string st;
    while(n--){
        cin >> s >> d;
        st = s;
        if(st == "+"){
            x += d;
        }
        else{
            if(d <= x){
                x -= d;
            }
            else{
                c ++;
            }
        }
    }
    cout << x << " " << c;
    return 0;
}