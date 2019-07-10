
#include<iostream>
#include<string>

using namespace std;

int main(){
   int q;
   cin>>q;
   
    for(int k=0; k<q; k++){
       
        int n,count=0;
        cin>>n;
        char input[n];
        char output[n];
        
        cin>>input>>output;
        
        int i=0;
        
        while(i!=n-1){
            if(input[i]==output[i]){
                count++;}
            else if(output[i]=='N'){
                count=count;
            }
            else{
                output[i+1]='N';
            }
            i++;
        }
        if(input[i]==output[i]){
            count++;
        }
        cout<<count<<endl;
   }
}
