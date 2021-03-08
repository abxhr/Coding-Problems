/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
	int n,k;
	cin >> n >> k;
	string a[n];
	for(int i=0;i<n;i++){
		cin >> a[i];
	}
	int count=0;
	for(int i=0;i<n;i++){
		int f=0;
		for(int j=0;j<=k;j++){
			stringstream ss;
			ss << j;
			string s = ss.str();
			if(a[i].find(string(s)) != -1) f++;
			if(f==k+1) count++;
		}
	}
	cout << count;
	return 0;
}