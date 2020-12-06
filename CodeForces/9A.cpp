#include <bits/stdc++.h>

using namespace std;

int main() {
    int y, w;
    cin >> y >> w;
    int g = (y>w?y:w);
    int chances = 0;
    for(int i = g; i<7; i++){
        if(i>=g) chances++;
    }
    int d = __gcd(chances, 6);
    int num = (chances!=0?(chances/d):0);
    int deno = (chances!=0?(6/d):1);
    cout << num << "/" << deno; 
    return 0;
}