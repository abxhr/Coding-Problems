/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    int a[n+1];
    int s = 0;
    int d = 0;
    int chk = 1;
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    int m;
    if (n % 2 !=0) m = (n/2) + 1;
    else m = (n/2);
    for(int i = 0,j = n - 1; i <= j; i++, j--){
        int largest = 0; 
        if(a[i] > a[j]){
            largest = a[i];
            j += 1;
        }
        else{
            largest = a[j];
            i -= 1;
        }
        if(chk){
            s += largest;
            chk = 0; 
        }
        else{
            d += largest;
            chk = 1;
        }
    }
    cout << s << " " << d;
}
    