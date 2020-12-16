#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int p[n+1],got[n+1];
    for(int i=1;i<=n;i++){
        cin >> p[i];
        got[i] = 0;
    }
    for(int i=1;i<=n;i++){
        got[p[i]] = i;
    }
    for(int i=1;i<=n;++i){
        cout << got[i] << " ";
    }
    return 0;
}
