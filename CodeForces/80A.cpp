#include <bits/stdc++.h>

using namespace std;

bool prime (int n){
  for (int z = 2;z<=sqrt(double(n));z++)
     if( n%z == 0 ) 
        return false;
   return true;
}

int main() {
	int n,m;
	cin >> n >> m;
	bool f = true;
	int next = 0;
	for(int i=n+1;i<=m;i++){
		if(prime(i)){
			next = i;
			break;
		}
	}
	if (next==m) cout << "YES";
	else cout << "NO";
	return 0;
}