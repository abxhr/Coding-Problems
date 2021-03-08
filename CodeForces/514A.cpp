/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
	long long x;
	cin >> x;
	int digit;
	int arr[20];
	int i=0;
	while(x>0){
		digit = x%10;
		if(9-digit<digit) arr[i] = 9-digit;
		else arr[i] = digit;
		i++;
		x = x/10;
	}
	if(arr[i-1]==0){
		cout << 9;
		i--;
	}
	for(int j=i-1;j>=0;--j){
		cout << arr[j];
	}
	return 0;
}