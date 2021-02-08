// Author: Abshar Mohammed Aslam, github.com/abxhr

#include <iostream>

int main(){
	int n;
	cin >> n;
	string s;
	cin >> s;
	for (int i = 0; i <= n; i++){
		if ((s[i] == 'H') && (s[i+1] == 'H')){
			cout << "NO\n";
			exit(0);
		}
		else if ((s[i] == '.')){
			s[i] = 'B';
		}
	}
	cout << "YES\n" << s;
}