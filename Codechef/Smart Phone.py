cus = int(input())
price = []
for _ in range(cus):
    price.append(int(input()))

price.sort(reverse=True)

rev_list=[]

for i,p in enumerate(price):
    rev_list.append(p*(i+1))
print(max(rev_list))
