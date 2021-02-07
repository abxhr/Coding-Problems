#include <iostream>

using namespace std;

int main(){
	int t;
	cin >> t;
	while(t--){
		int g, p, n;
		cin >> g >> p >> n;
		int q1 = 0, q2 = 0;
		while(n--){
			int i;
			cin >> i;
			q1 += i;
			cin >> i;
			q2 += i;
		}

		int first_way = g*q1 + p*q2;
		int second_way = p*q1 + g*q2;

		if (first_way < second_way) cout << first_way << "\n";
		else cout << second_way << "\n";
	}
	return 0;
}