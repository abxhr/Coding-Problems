#include<bits/stdc++.h>

using namespace std;

class Box{
    private:
        long long l, b, h;
    public:
        Box(){
            l = 0;
            b = 0;
            h = 0;
        }
        
        Box(int L, int B, int H){
            l = L;
            b = B;
            h = H;
        }
        
        Box(Box &a){
            l = a.getLength();
            b = a.getBreadth();
            h = a.getHeight();
        }
        
        int getLength(){
            return l;
        }
        
        int getBreadth(){
            return b;
        }
        
        int getHeight(){
            return h;
        }
        
        long long CalculateVolume(){
            return l*b*h;
        }
        
        friend bool operator<(Box &a, Box &b){
            if((a.l < b.l) || (a.b < b.b && a.l == b.l) || (a.h < b.h && a.l == b.l && a.b == b.b)) return true;
            else return false;
        }
        
        friend ostream & operator <<(ostream &out, const Box &a){
            out << a.l << " " << a.b << " " << a.h;
            return out;
        }
};


void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}