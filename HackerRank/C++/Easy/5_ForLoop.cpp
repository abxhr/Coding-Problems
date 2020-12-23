#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int a,b;
    cin >> a >> b;
    string nums [] = {"","one", "two","three","four","five","six", "seven","eight","nine"};
    for(int i=a;i<=b;i++){
        if(i<=9) cout << nums[i];
        else{
            if(i%2==0) cout << "even";
            else cout << "odd";
        }
        cout << "\n";
    }
    return 0;
}