/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
	int n,k;
	cin >> n >> k;
	int r[2*n+1];
	int max = -1;
	for(int i=0;i<2*n+1;i++){
		cin >> r[i];
	}
	int place[2*n+1] = {0};
	for(int i=1;i<2*n;i++){
		if((r[i-1]+1 < r[i]) && (r[i+1]+1 < r[i])) place[i]--;
	}
	int i = 0;
	while(k--){
		if(place[i] == 0) k++;
		cout << r[i] + place[i] << " ";
		i++;
	}
	for(;i<2*n+1;i++){
		cout << r[i] << " ";
	}
	return 0;
}