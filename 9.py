def egcd(a,b):
    if b==0:
        return a,1,0
    g,x1,y1=egcd(b,a%b)
    return g,y1,x1-(a//b)*y1

while True:
    print("\n1.Find 2.Exit")
    ch=int(input())
    if ch==2: break
    a,b=map(int,input("a b: ").split())
    print("GCD,x,y =",egcd(a,b))
