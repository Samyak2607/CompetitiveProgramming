# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
d={}
for i in range(n):
    name,phn=map(str,input().split())
    d[name]=phn
for i in range(n):
    name=input()
    if name in d:
        print(name+'='+d[name])
    else:
        print('Not found')
