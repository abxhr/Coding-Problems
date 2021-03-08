// Author: Abshar Mohammed Aslam, github.com/abxhr

#include <iostream>

using namespace std;

int main(){
	int n;
	cin >> n;
	int f = 1;
	for (int i = 2; i <= n; i++) f *= i;
	cout << f;
	return 0;
}