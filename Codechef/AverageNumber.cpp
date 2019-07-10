#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int n,k,v;
	    cin>>n>>k>>v;
	    int a[n],sum=0;
	    for(int i=0;i<n;i++){
	        cin>>a[i];
	        sum+=a[i];
	    }
	    int t,d,ans;
	    t=(n+k)*v;
	    d=t-sum;
	    if(d%k==0 && d>0)
            ans=d/k;
        else
            ans=-1;
    cout<<ans<<endl;
	}
	return 0;
}
