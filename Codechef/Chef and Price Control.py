for _ in range(int(input())):
    n,k = map(int, input().split())
    price = list(map(int, input().split()))
    rev_loss=0

    for p in price:
        if p>k:
            rev_loss+=p-k
    print(rev_loss)
