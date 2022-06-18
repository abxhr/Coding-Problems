// Author: Abshar Mohammed Aslam, github.com/abxhr

#include <iostream>

using namespace std;

int main(){
	int l, n;
	cin >> l >> n;
	while(n--){
		int w, h;
		cin >> w >> h;
		if ((w < l) || (h < l)) cout << "UPLOAD ANOTHER\n";
		else{
			if (w == h) cout << "ACCEPTED\n";
			else cout << "CROP IT\n";
		}
	}
	return 0;
}
