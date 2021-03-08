#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> v;
    for(int i=0;i<n;i++){
        int temp;
        cin >> temp;
        v.push_back(temp);
    }
    int x;
    cin >> x;
    x--;
    v.erase(v.begin()+x);
    int a, b;
    cin >> a >> b;
    a--; b--;
    v.erase(v.begin()+a, v.begin()+b);
    cout << v.size() << "\n";
    for(int i=0;i<v.size();i++){
        cout << v[i] << " ";
    }
    return 0;
}
