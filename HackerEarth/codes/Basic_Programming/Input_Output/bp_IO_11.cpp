// Author: Abshar Mohammed Aslam, github.com/abxhr

#include <iostream>

using namespace std;

int main(){
	string s;
	cin >> s;
	int z_count = 0, o_count = 0;
	for (int i = 0; i <= s.length(); i++){
		if (s[i] == 'z') z_count++;
		else if (s[i] == 'o') o_count++;
	}
	if ((2*z_count) == o_count) cout << "Yes";
	else cout << "No";
	return 0;
}