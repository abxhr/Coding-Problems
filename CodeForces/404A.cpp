/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	cin >> n;
	char a[n][n];
	for(int i=0;i<n;i++){
		string t;
		cin >> t;
		for(int j=0;j<n;j++){
			a[i][j] = (char)t[j];
		}
	}

	int c = 0;
	char d1 = a[0][0];
	char d2 = a[0][n-1];
	char oth = a[0][1];
 
	if (d1 == oth) c = 1;

	if (d1 != d2) c = 1;
	else{
		for(int i=0;((i<n)&&(c==0));i++){
			for(int j=0;((j<n)&&(c==0));j++){
				if((i==j)||(i+j==n-1)){
					if (a[i][j]!=d1){
						c = 1;
						break;
					} 
				}
				
				else{
					if(a[i][j]!=oth){
						c = 1;
						break;
					}
				}
			}
		}
	}

	(c==1)?cout<<"NO":cout<<"YES";
	return 0;
}