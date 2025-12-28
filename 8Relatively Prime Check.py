def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

while True:
    print("\n1.Check 2.Exit")
    ch=int(input())
    if ch==2: break
    a,b=map(int,input("Numbers: ").split())
    print("Relatively Prime" if gcd(a,b)==1 else "Not Relatively Prime")
