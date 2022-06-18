// Author: Abshar Mohammed Aslam, github.com/abxhr

#include <iostream>
#include <cmath>

using namespace std;

int main(){
	string seat[] = {"WS", "MS", "AS"};
	int ipos = 1;

	int t;
	cin >> t;
	while(t--){
		int n, opp_num;
		cin >> n;
		if (n%12!=0){
			opp_num = (floor(n/12)+1)*12 - n%12 + 1;
		}
		else{
			opp_num = n - 11;
		}
		cout << opp_num << " ";
		if ((n%6 == 1) || (n%6 == 0)) cout << "WS" << "\n";
		else if ((n%6 == 2) || (n%6 == 5)) cout << "MS" << "\n";
		else cout << "AS" << "\n";
	}
	return 0;
}