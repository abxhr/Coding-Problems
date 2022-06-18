#include<bits/stdc++.h>

using namespace std;

int main(){
  long long a1,a2,a3,a4;
  cin >> a1 >> a2 >> a3 >> a4;
  long long t = min(a1,a2);
  t = min(t,a3);
  t = min(t,a4);
  cout << t;
  return 0;
}