file=open("comment.txt",'r')
s=file.read()
count_slash_n=0
count1=0
count2=0
error=0
j=0
while(j<(len(s)-1)):
    if(s[j]=='/' and s[j+1]=='/'):
        k=j+2
        count1+=1
        ans2=""
        print("single Line commment is : ",end="")
        while(k<len(s) and s[k]!="\n"):
            ans2+=s[k]
            k+=1
        j=k
        print(ans2.strip())
        count_slash_n+=1
    elif(s[j]=='/' and s[j+1]=='*'):
        k=j+2
        count2+=1
        ans=""
        check=1
        if(k+1>=len(s)):
            check=0
            count2-=1
            error+=1
            count_slash_n+=1
            print("Error!! You have not closed multi line comment properly in line :",count_slash_n)
        else:
            while(not(s[k]=='*' and s[k+1]=='/')):
                if(k==len(s)-2):
                    error+=1
                    count_slash_n+=1
                    print("Error!! You have not closed multi line comment properly in line :",count_slash_n)
                    count2-=1
                    check=0
                    break
                else:
                    if(s[k]=="\n"):
                        count_slash_n+=1
                    ans+=s[k]
                k+=1
            if(check==1):
                print("Multi Line commment is :",ans.strip())
                count_slash_n+=1
            j=k
    j+=1

print("Number of single comment : ",count1)
print("Number of multi line comment",count2)
print("Number of errors :",error)
