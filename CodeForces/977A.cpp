#include <iostream>

using namespace std;

int main(){
    int n, k;
    cin >> n >> k;
    while(k--){
        int last = n%10;
        if (last == 0) n /= 10;
        else n -= 1; 
    }
    cout << n;
    return 0;
}