t = int(input())
for _ in range(t):
    n = input()
    l = []
    for i in range(len(n)):
        temp = n[:i]+n[i+1:]
        l.append(int(temp))
    print(min(l))
        
