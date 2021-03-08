// Author: Abshar Mohammed Aslam, github.com/abxhr

#include <iostream>

using namespace std;

int main(){
	int l, r, k;
	cin >> l >> r >> k;
	int count = 0;
	for (int i = l; i <= r; i++){
		if (i%k == 0) count++;
	} 
	cout << count;
	return 0;
}