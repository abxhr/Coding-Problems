/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int a[5][5];
    int ci, cj;
    for (int i =0; i < 5; ++i){
        for(int j = 0; j < 5; ++j){
            cin >> a[i][j];
            if (a[i][j] == 1){
                ci = i;
                cj = j;
            }
            }
        }
    cout << abs(3 - ci -1) + abs(3 - cj -1);
    }