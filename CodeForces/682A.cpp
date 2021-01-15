#include <bits/stdc++.h>

using namespace std;

int main() {
	long long n,m;
	cin >> n >> m;
	long long int modN[5] = {0};
	long long int modM[5] = {0};
	for(int i=1;i<=m;i++) modM[i%5]++;
	for(int i=1;i<=n;i++) modN[i%5]++;
	long long int val = modN[0] * modM[0];
	val += modN[1] * modM[4];
	val += modN[2] * modM[3];
	val += modN[3] * modM[2];
	val += modN[4] * modM[1];
	cout << val;
	return 0;
}
