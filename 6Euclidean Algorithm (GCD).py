while True:
    print("\n1.Find GCD 2.Exit")
    ch=int(input())
    if ch==2: break
    a,b=map(int,input("Enter numbers: ").split())
    while b:
        a,b=b,a%b
    print("GCD:",a)
