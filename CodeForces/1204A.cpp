/*
Author: Abshar Mohammed Aslam, github.com/abxhr
*/

#include <bits/stdc++.h>

using namespace std;

int main(){
	string s;
	cin>>s;
	long long int p=s.length();
	if(p%2==0) cout<<(p/2);
	else{
		int count1=0;
		for(int i=0;i<s.length();i++){
			if(s[i]=='1') count1++;
		}
		if(count1>1){
			int ans=p/2;
			cout<<(ans+1);
		}
		else{
			int ans=p/2;
			cout<<ans;
		}
	}
	return 0;
}

