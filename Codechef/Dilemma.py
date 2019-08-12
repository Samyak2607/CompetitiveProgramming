#include <iostream>
#include <cstring>
using namespace std;

int main() {
	int tc;
	cin>>tc;
	for(int i=0;i<tc;i++){
	    string s;
	    int count=0;
	    cin>>s;
	    for(int j=0;j<s.size();j++){
	        if(s[j]=='1')
	            count++;
	        
	    }
	    
	    if(count%2==0)
	        cout<<"LOSE"<<endl;
	    else
	        cout<<"WIN"<<endl;
	}
	return 0;
}
