while True:
    print("\n1.Find Inverse 2.Exit")
    ch=int(input())
    if ch==2: break
    a,n=map(int,input("a n: ").split())
    print("Additive Inverse:",(n-a)%n)
