#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int main() {
    int q;
    cin >> q;
    map<string,int> m;
    for(int i=0;i<q;i++){
        int a;
        string s;
        cin >> a;
        switch(a){
            case 1:
                int t;
                cin >> s >> t;
                m[s] += t;
                break;
            case 2:
                cin >> s;
                m.erase(s);
                break;
            case 3:
                cin >> s;
                map<string,int>::iterator itr=m.find(s);
                if(itr == m.end()) cout << "0" << "\n";
                else cout << m[s] << "\n";
                break;
        }
    }
    return 0;
}