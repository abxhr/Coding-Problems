#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> bf;
    vector<int> af;
    for(int i=0;i<n;i++){
        int t;
        cin >> t;
        bf.push_back(t);
        cin >> t;
        af.push_back(t);
    }
    int c = 0;
    for(int i=0;i<n;i++){
        if(bf[i]==af[i]){
            for(int j=0;j<i;j++){
                if(bf[j] < bf[i]){
                    c = 1;
                    break;
                }
            }
        }
        else{
            c = -1;
            break;
        }
    }
    if(c==0) cout << "maybe";
    else if(c==1) cout << "unrated";
    else cout << "rated";
    return 0;
}