#include <bits/stdc++.h>

using namespace std;

int vsum(vector<int> v, int i){
    int s=0;
    for(;i<v.size();i++){
        s += v[i];
    }
    return s;
}

int main() {
    int n;
    cin >> n;
    vector<int> a;
    for(int i=0;i<n;i++){
        int t;
        cin >> t;
        a.push_back(t);
    }
    sort(a.begin(), a.end(), greater<int>());
    int tc=0;
    int cv=0;
    for(;tc<n;tc++){
        cv += a[tc];
        if(cv > vsum(a,tc+1)) break;
    }
    tc++;
    cout << tc << "\n";
    return 0;
}