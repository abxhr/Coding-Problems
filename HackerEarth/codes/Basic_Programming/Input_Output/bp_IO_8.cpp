// Author: Abshar Mohammed Aslam, gtihub.com/abxhr

#include <iostream>
#include <cctype>

using namespace std;

int main(){
	string a;
	cin >> a;
	for (int i = 0; i < a.length(); i++){
		if (isupper(a[i])) a[i] =  tolower(a[i]);
		else a[i] = toupper(a[i]);
	}
	cout << a;
	return 0;
}