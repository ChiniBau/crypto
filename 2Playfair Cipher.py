def matrix(key):
    key = key.replace("J","I")
    seen = ""
    for c in key+"ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in seen:
            seen += c
    return [seen[i:i+5] for i in range(0,25,5)]

def pos(m):
    return {m[r][c]:(r,c) for r in range(5) for c in range(5)}

def playfair(text,key,mode):
    m = matrix(key)
    p = pos(m)
    res = ""
    d = 1 if mode=="e" else -1
    for i in range(0,len(text),2):
        a,b = text[i],text[i+1]
        r1,c1 = p[a]; r2,c2 = p[b]
        if r1==r2:
            res+=m[r1][(c1+d)%5]+m[r2][(c2+d)%5]
        elif c1==c2:
            res+=m[(r1+d)%5][c1]+m[(r2+d)%5][c2]
        else:
            res+=m[r1][c2]+m[r2][c1]
    return res

while True:
    print("\n1.Encrypt 2.Decrypt 3.Exit")
    ch=int(input())
    if ch==3: break
    t=input("Text (even length): ").upper().replace("J","I")
    k=input("Key: ").upper()
    print(playfair(t,k,"e" if ch==1 else "d"))
