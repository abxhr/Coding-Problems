/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main()
{
    string s,e,a="",b="";
    cin >> s >> e;
    int i = 0;
    while(i<s.size() && s[i]!='|'){
        a+=s[i];
        i++;
    }
    i++;
    while(i<s.size()){
        b+=s[i];
        i++;
    }

    if((a.size()+b.size()+e.size())%2){
        cout << "Impossible";
        return 0;
    }

    int n = (a.size()+b.size()+e.size())/2;
    int size = n - a.size();

    i=0;

    while(size-- && i<e.size()){
        a+=e[i];
        i++;
    }

    size = n - b.size();

    while(size-- && i<e.size()){
        b+=e[i];
        i++;
    }

    if(a.size()!=b.size()) cout << "Impossible";
    else cout << a << "|" << b;
    return 0;
}
