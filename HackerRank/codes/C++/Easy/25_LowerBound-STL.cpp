// Author: Abshar Mohammed Aslam, github.com/abxhr

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    cin >> n;
    vector<int> arr;
    for (int i = 0; i < n; i++){
        int val;
        cin >> val;
        arr.push_back(val);
    }
    int q;
    cin >> q;
    while(q--){
        int y;
        cin >> y;
        vector<int>::iterator low = lower_bound(arr.begin(), arr.end(), y);
        if (arr[low - arr.begin()] == y)
           cout << "Yes " << (low - arr.begin()+1) << "\n";
        else
           cout << "No " << (low - arr.begin()+1) << "\n";
    }
    return 0;
}
