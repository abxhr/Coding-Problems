#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,q;
    cin >> n >> q;
    int k;
    int in;
    vector<vector<int> > a;
    for(int i=0;i<n;i++){
        cin >> k;
        vector<int> temp;
        for(int j=0;j<k;j++){
            cin >> in;
            temp.push_back(in);
        }
        a.push_back(temp);
    }
    int r,c;
    for(int i=0;i<q;i++){
        cin >> r >> c;
        cout << a[r][c] << "\n";
    }
    return 0;
}
