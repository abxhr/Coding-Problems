// Author: Abshar Mohammed Aslam, github.com/abxhr

#include <iostream>

using namespace std;

int main(){
	string a;
	cin >> a;
	int len = a.length();
	for (int i = 0; i < (int)(len/2); i++){
		if (a[i] != a[len-1-i]){
			cout << "NO";
			exit(0);
		}
	}
	cout << "YES";
	return 0;
}