#include <iostream>
using namespace std;

#define inte unsigned long long int

int main() {
	inte q;
	cin>>q;
	while(q--){
	    inte n;
	    cin>>n;
	    inte a=n;
	    inte sum=0,result=0,rem=0;
	    while(n!=0){
	        sum+=n%10;
	        n=n/10;
	    }
	    rem=sum%10!=0 ? (10-sum%10):0;
	    result=a*10+rem;
	    cout<<result<<endl;
	}
	return 0;
}
