/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int k,r;
    cin >> k >> r;
    bool f = true;
    for(int i = 1;f;i++){
        if((k*i) == (((k*i)/10)*10)){
            cout << i;
            f = false;
        }
        else if ((k*i) == ((((k*i)/10)*10) + r)){
            cout << i;
            f = false;
        }
    }
    return 0;
}