#include <bits/stdc++.h>

using namespace std;

int main() {
	long long n;
	cin >> n;
	long long faces=0;
	string a;
	for(int i=0;i<n;i++){
		cin >> a;
		if(a.compare("Tetrahedron")==0) faces+=4;
		else if(a.compare("Cube")==0) faces+=6;
		else if(a.compare("Octahedron")==0) faces+=8;
		else if(a.compare("Dodecahedron")==0) faces+=12;
		else faces+=20;
	}
	cout << faces;
	return 0;
}