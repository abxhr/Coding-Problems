/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
	long long int l,r;
	cin >> l >> r;
	if (l%2 != 0) l++;
	if (l+2>r) cout << -1;
	else cout << l << " " << l+1 << " " << l+2;
	return 0;
}