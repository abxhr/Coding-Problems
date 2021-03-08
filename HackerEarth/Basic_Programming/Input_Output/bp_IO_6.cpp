// Author: Abshar Mohammed Aslam, github.com/abxhr

#include <iostream>
#include <cmath>

using namespace std;

int main(){
	int n;
	cin >> n;
	int a;
	long long answer = 1;
	for (int i = 0; i < n; i++){
		cin >> a;
		answer = (answer * a) % ((long long)pow(10, 9) + 7);
	}
	cout << answer;
	return 0;
}